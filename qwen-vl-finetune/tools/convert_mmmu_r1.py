"""Convert xDAN-Vision/MMMU-LLM-R1-format to the qwen-vl-finetune JSONL schema.

Output layout (under --out_dir):
  images/<original_filename>.png    one file per image referenced by the dataset
  train.jsonl                        one sample per line: {image, conversations, source}

Each conversation has two turns:
  human: <system_preamble>\n\n<user_text_with_<image>_placeholders>
  gpt:   <assistant_message_with_<think>/<answer>_tags>

Schema matches qwenvl/data/data_processor.py's `_build_messages` /
`check_image_aligned`: number of `<image>` placeholders in the human turn equals
len(image list). Image paths are stored relative to --out_dir/images, so the
dataset registration must point `data_path` at --out_dir/images.
"""
import argparse
import json
import re
import sys
from pathlib import Path

from datasets import load_dataset
from tqdm import tqdm


IMG_KEYS = [f"image_{i}" for i in range(1, 8)]


def extract_user_text(message_field: str) -> tuple[str, str, str]:
    """Return (system_text, user_text, assistant_text). `message_field` is double-JSON-encoded."""
    msg = json.loads(json.loads(message_field))
    system_text = ""
    user_text_parts: list[str] = []
    assistant_text = ""
    for turn in msg:
        role = turn["role"]
        content = turn["content"]
        if role == "system":
            system_text = content if isinstance(content, str) else _join_text_parts(content)
        elif role == "user":
            user_text_parts.append(content if isinstance(content, str) else _join_text_parts(content))
        elif role == "assistant":
            assistant_text = content if isinstance(content, str) else _join_text_parts(content)
    return system_text.strip(), "\n".join(p for p in user_text_parts if p).strip(), assistant_text.strip()


def _join_text_parts(parts) -> str:
    out = []
    for part in parts:
        if isinstance(part, dict) and part.get("type") == "text":
            out.append(part.get("text", ""))
    return "\n".join(out)


def normalize_image_markers(text: str, n_images: int) -> str:
    """Replace MMMU-style `<image N>` markers with `<image>` placeholders.

    If the text references `<image N>` for indices that exceed n_images,
    the extras are dropped. If fewer markers than images are present in the
    text, the missing ones are appended at the start so placeholder count
    matches image count (loader requires exact match).
    """
    pattern = re.compile(r"<image\s*(\d+)>")
    seen: list[int] = []

    def _sub(m: re.Match) -> str:
        idx = int(m.group(1))
        if idx < 1 or idx > n_images:
            return ""
        seen.append(idx)
        return "<image>"

    text = pattern.sub(_sub, text)

    missing = [i for i in range(1, n_images + 1) if i not in seen]
    if missing:
        prefix = "".join("<image>\n" for _ in missing)
        text = prefix + text

    extras = len(seen) - n_images
    if extras > 0:
        for _ in range(extras):
            text = text.replace("<image>", "", 1)

    return text


def convert(out_dir: Path, hf_id: str, split: str, limit: int | None) -> None:
    img_dir = out_dir / "images"
    img_dir.mkdir(parents=True, exist_ok=True)
    jsonl_path = out_dir / f"{split}.jsonl"

    ds = load_dataset(hf_id, split=split)
    if limit is not None:
        ds = ds.select(range(min(limit, len(ds))))

    kept = 0
    skipped_unaligned = 0
    skipped_no_assistant = 0
    with jsonl_path.open("w") as fout:
        for i, row in enumerate(tqdm(ds, desc="converting")):
            images = [(k, row[k]) for k in IMG_KEYS if row[k] is not None]
            image_paths: list[str] = []
            for k, img in images:
                orig_path = img.get("path") or f"row{i:05d}_{k}.png"
                rel_path = orig_path  # already unique within the dataset (e.g. validation_Agriculture_16_1.png)
                dst = img_dir / rel_path
                if not dst.exists():
                    dst.write_bytes(img["bytes"])
                image_paths.append(rel_path)

            try:
                system_text, user_text, assistant_text = extract_user_text(row["message"])
            except Exception as e:
                print(f"[row {i}] failed to parse message: {e}", file=sys.stderr)
                continue

            if not assistant_text:
                skipped_no_assistant += 1
                continue

            user_text = normalize_image_markers(user_text, len(image_paths))

            n_placeholders = user_text.count("<image>")
            if n_placeholders != len(image_paths):
                skipped_unaligned += 1
                continue

            if system_text:
                human_value = f"{system_text}\n\n{user_text}"
            else:
                human_value = user_text

            record = {
                "conversations": [
                    {"from": "human", "value": human_value},
                    {"from": "gpt", "value": assistant_text},
                ],
                "source": row.get("source", ""),
            }
            if image_paths:
                record["image"] = image_paths if len(image_paths) > 1 else image_paths[0]

            fout.write(json.dumps(record, ensure_ascii=False) + "\n")
            kept += 1

    print(f"wrote {kept} samples to {jsonl_path}")
    print(f"skipped (placeholder/image misalignment): {skipped_unaligned}")
    print(f"skipped (no assistant message): {skipped_no_assistant}")
    print(f"images under {img_dir}")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--hf_id", default="xDAN-Vision/MMMU-LLM-R1-format")
    ap.add_argument("--split", default="train")
    ap.add_argument("--out_dir", required=True, type=Path)
    ap.add_argument("--limit", type=int, default=None, help="cap number of samples (smoke testing)")
    args = ap.parse_args()
    convert(args.out_dir, args.hf_id, args.split, args.limit)


if __name__ == "__main__":
    main()
