import json
import hashlib
import os
from bisect import bisect_right
from collections import OrderedDict
import random
import logging
import re
import time
import itertools
from dataclasses import dataclass, field
from typing import Dict, Optional, Sequence, List, Tuple, Any
from collections.abc import Sequence
from pathlib import Path

import numpy as np
import torch
from torch.utils.data import Dataset

import transformers

from . import data_list
from .rope2d import get_rope_index_25, get_rope_index_2, get_rope_index_3
try:
    import torch.distributed as dist
except Exception:
    dist = None

IGNORE_INDEX = -100
IMAGE_TOKEN_INDEX = 151655
VIDEO_TOKEN_INDEX = 151656
DEFAULT_IMAGE_TOKEN = "<image>"
DEFAULT_VIDEO_TOKEN = "<video>"

local_rank = int(os.getenv("RANK", "0"))


def rank0_print(*args):
    if local_rank == 0:
        print(*args)


def read_jsonl(path):
    with open(path, "r") as f:
        return [json.loads(line) for line in f if check_image_aligned(json.loads(line))]

def lazy_read_jsonl(path, chunk_size):
    lines = []
    with open(path, "r") as f:
        for line in f:
            item = json.loads(line)
            if check_image_aligned(item):
                lines.append(item)
            else:
                print(f"Skipping image not aligned: {item}")
            if len(lines) >= chunk_size:
                yield lines
                lines = []

def check_image_aligned(item) -> bool:
    images = item.get("image") or []
    if isinstance(images, str):
        images = [images]

    num_images = len(images)
    conversations = item['conversations'].copy()
    last_user_message = ""
    while conversations:
        conv = conversations.pop(-1)
        if conv['from'] == 'human':
            last_user_message = conv['value']
            break  
    num_image_placeholders = last_user_message.count('<image>')

    return num_images == num_image_placeholders

def _make_abs_paths(base: Path, files: str) -> str:
    return f"{(base / files).resolve()}"


def update_processor_pixels(processor, data_args):
    logger = logging.getLogger(__name__)

    # --- Image Processor ---
    ip = processor.image_processor
    rank0_print("=== BEFORE IMAGE PROCESSOR PARAMETERS ===")
    rank0_print(f"Image min_pixels: {getattr(ip, 'min_pixels', 'N/A')}")
    rank0_print(f"Image max_pixels: {getattr(ip, 'max_pixels', 'N/A')}")
    rank0_print(f"ip.size: {ip.size}")
    rank0_print(f"Image size (shortest_edge): {ip.size.get('shortest_edge', 'N/A')}")
    rank0_print(f"Image size (longest_edge):  {ip.size.get('longest_edge', 'N/A')}")

    if hasattr(ip, "min_pixels") and hasattr(ip, "max_pixels"):
        ip.min_pixels = data_args.min_pixels
        ip.max_pixels = data_args.max_pixels
        rank0_print(f"✅ Updated image_processor min_pixels to {data_args.min_pixels}")
        rank0_print(f"✅ Updated image_processor max_pixels to {data_args.max_pixels}")

    if hasattr(ip, "size") and isinstance(ip.size, dict):
        ip.size["shortest_edge"] = data_args.min_pixels
        ip.size["longest_edge"] = data_args.max_pixels
        rank0_print(
            f"✅ Updated image_processor size['shortest_edge'] to {data_args.min_pixels}"
        )
        rank0_print(
            f"✅ Updated image_processor size['longest_edge'] to {data_args.max_pixels}"
        )

    rank0_print("=== AFTER IMAGE PROCESSOR PARAMETERS ===")
    rank0_print(f"Image min_pixels: {getattr(ip, 'min_pixels', 'N/A')}")
    rank0_print(f"Image max_pixels: {getattr(ip, 'max_pixels', 'N/A')}")
    rank0_print(f"Image size (shortest_edge): {ip.size.get('shortest_edge', 'N/A')}")
    rank0_print(f"Image size (longest_edge):  {ip.size.get('longest_edge', 'N/A')}")

    # --- Video Processor ---
    if hasattr(processor, "video_processor") and processor.video_processor is not None:
        vp = processor.video_processor
        rank0_print("\n=== BEFORE VIDEO PROCESSOR PARAMETERS ===")
        rank0_print(f"Video min_pixels: {getattr(vp, 'min_pixels', 'N/A')}")
        rank0_print(f"Video max_pixels: {getattr(vp, 'max_pixels', 'N/A')}")
        rank0_print(f"Video min_frames: {getattr(vp, 'min_frames', 'N/A')}")
        rank0_print(f"Video max_frames: {getattr(vp, 'max_frames', 'N/A')}")
        rank0_print(f"Video fps: {getattr(vp, 'fps', 'N/A')}")
        rank0_print(
            f"Video size (shortest_edge): {vp.size.get('shortest_edge', 'N/A')}"
        )
        rank0_print(f"Video size (longest_edge):  {vp.size.get('longest_edge', 'N/A')}")

        if hasattr(vp, "min_pixels") and hasattr(vp, "max_pixels"):
            vp.min_pixels = data_args.video_min_pixels
            vp.max_pixels = data_args.video_max_pixels
            rank0_print(
                f"✅ Updated Qwen2-VL video_processor min_pixels to {data_args.video_min_pixels}"
            )
            rank0_print(
                f"✅ Updated Qwen2-VL video_processor max_pixels to {data_args.video_max_pixels}"
            )

        if hasattr(vp, "min_frames") and hasattr(vp, "max_frames"):
            vp.min_frames = data_args.video_min_frames
            vp.max_frames = data_args.video_max_frames
            rank0_print(
                f"✅ Updated video_processor min_frames to {data_args.video_min_frames}"
            )
            rank0_print(
                f"✅ Updated video_processor max_frames to {data_args.video_max_frames}"
            )

        if hasattr(vp, "fps"):
            vp.fps = data_args.video_fps
            rank0_print(f"✅ Updated video_processor fps to {data_args.video_fps}")

        if hasattr(vp, "size") and isinstance(vp.size, dict):
            vp.size["shortest_edge"] = data_args.video_min_pixels
            vp.size["longest_edge"] = data_args.video_max_pixels
            rank0_print(
                f"✅ Updated Video size (shortest_edge): {vp.size.get('shortest_edge', 'N/A')}"
            )
            rank0_print(
                f"✅ Updated Video size (longest_edge):  {vp.size.get('longest_edge', 'N/A')}"
            )

        rank0_print("=== AFTER VIDEO PROCESSOR PARAMETERS ===")
        rank0_print(f"Video min_pixels: {getattr(vp, 'min_pixels', 'N/A')}")
        rank0_print(f"Video max_pixels: {getattr(vp, 'max_pixels', 'N/A')}")
        rank0_print(f"Video min_frames: {getattr(vp, 'min_frames', 'N/A')}")
        rank0_print(f"Video max_frames: {getattr(vp, 'max_frames', 'N/A')}")
        rank0_print(f"Video fps: {getattr(vp, 'fps', 'N/A')}")
        rank0_print(
            f"Video size (shortest_edge): {vp.size.get('shortest_edge', 'N/A')}"
        )
        rank0_print(f"Video size (longest_edge):  {vp.size.get('longest_edge', 'N/A')}")

    return processor


def _build_messages(item: Dict[str, Any], base_path: Path) -> List[Dict[str, Any]]:
    # Extract and normalize images and videos
    images = item.get("image") or []
    if isinstance(images, str):
        images = [images]

    videos = item.get("video") or []
    if isinstance(videos, str):
        videos = [videos]

    # Build media pools with absolute paths
    image_pool = [
        {"type": "image", "image": _make_abs_paths(base_path, img)} for img in images
    ]
    video_pool = [
        {"type": "video", "video": _make_abs_paths(base_path, vid)} for vid in videos
    ]

    messages = []
    for turn in item["conversations"]:
        role = "user" if turn["from"] == "human" else "assistant"
        text: str = turn["value"]

        if role == "user":
            content = []
            # Split text by <image> or <video> placeholders while keeping delimiters
            text_parts = re.split(r"(<image>|<video>)", text)

            for seg in text_parts:
                if seg == "<image>":
                    if not image_pool:
                        raise ValueError(
                            "Number of <image> placeholders exceeds the number of provided images"
                        )
                    content.append(image_pool.pop(0))
                elif seg == "<video>":
                    if not video_pool:
                        raise ValueError(
                            "Number of <video> placeholders exceeds the number of provided videos"
                        )
                    content.append(video_pool.pop(0))
                elif seg.strip():
                    content.append({"type": "text", "text": seg.strip()})

            messages.append({"role": role, "content": content})
        else:
            # Assistant messages contain only text
            messages.append({"role": role, "content": [{"type": "text", "text": text}]})

    # Check for unused media files
    if image_pool:
        raise ValueError(
            f"{len(image_pool)} image(s) remain unused (not consumed by placeholders)"
        )
    if video_pool:
        raise ValueError(
            f"{len(video_pool)} video(s) remain unused (not consumed by placeholders)"
        )

    return messages


def preprocess_qwen_visual(
    sources,
    processor,
) -> Dict:
    if len(sources) != 1:
        raise ValueError(f"Expected 1 source, got {len(sources)}")

    source = sources[0]
    base_path = Path(source.get("data_path", ""))
    messages = _build_messages(source, base_path)

    full_result = processor.apply_chat_template(
        messages, tokenize=True, return_dict=True, return_tensors="pt"
    )

    input_ids = full_result["input_ids"]
    if isinstance(input_ids, list):
        input_ids = torch.tensor(input_ids).unsqueeze(0)

    labels = torch.full_like(input_ids, IGNORE_INDEX)

    input_ids_flat = input_ids[0].tolist()
    L = len(input_ids_flat)
    pos = 0
    while pos < L:
        if input_ids_flat[pos] == 77091:
            ans_start = pos + 2
            ans_end = ans_start
            while ans_end < L and input_ids_flat[ans_end] != 151645:
                ans_end += 1
            if ans_end < L:
                labels[0, ans_start : ans_end + 2] = input_ids[
                    0, ans_start : ans_end + 2
                ]
                pos = ans_end
        pos += 1

    full_result["labels"] = labels
    full_result["input_ids"] = input_ids
    return full_result


class LazySupervisedDataset(Dataset):
    """Dataset for supervised fine-tuning."""

    def __init__(self, processor, data_args):
        super(LazySupervisedDataset, self).__init__()

        print("=" * 80)
        print("INITIALIZING LazySupervisedDataset")
        print("=" * 80)

        dataset = data_args.dataset_use.split(",")
        print(f"Dataset names from args: {dataset}")
        dataset_list = data_list(dataset)
        rank0_print(f"Loading datasets: {dataset_list}")
        self.video_max_total_pixels = getattr(
            data_args, "video_max_total_pixels", 1664 * 28 * 28
        )
        self.video_min_total_pixels = getattr(
            data_args, "video_min_total_pixels", 256 * 28 * 28
        )
        self.model_type = data_args.model_type
        if data_args.model_type == "qwen3vl":
            self.get_rope_index = get_rope_index_3
        elif data_args.model_type == "qwen2.5vl":
            self.get_rope_index = get_rope_index_25
        elif data_args.model_type == "qwen2vl":
            self.get_rope_index = get_rope_index_2
        else:
            raise ValueError(f"model_type: {data_args.model_type} not supported")

        self.lazy_read_jsonl = getattr(data_args, "lazy_read_jsonl", False)
        self.prefetch_size = getattr(data_args, "prefetch_size", 1000)
        self._max_cached_chunks = getattr(data_args, "prefetch_cache_chunks", 8)
        self._seed = getattr(data_args, "seed", 42)
        print(f"Lazy loading mode: {self.lazy_read_jsonl}")
        print(f"Prefetch size: {self.prefetch_size}")
        print(f"Max cached chunks: {self._max_cached_chunks}")

        # Eagerly loaded samples (JSON files or when lazy disabled)
        list_data_dict = []

        # Lazy JSONL metadata when lazy mode is enabled
        self._lazy_files_meta = []  # list of dicts with jsonl metadata
        self._lazy_prefix_sums = []  # cumulative effective lengths across lazy jsonl files
        self._chunk_cache = OrderedDict()  # (file_idx, chunk_id) -> List[dict]

        if not self.lazy_read_jsonl:
            # Original eager loading behavior
            print("Using EAGER loading mode")
            for idx, data in enumerate(dataset_list):
                print(f"[{idx+1}/{len(dataset_list)}] Loading dataset: {data['annotation_path']}")
                file_format = data["annotation_path"].split(".")[-1]
                if file_format == "jsonl":
                    print(f"  Reading JSONL file...")
                    annotations = read_jsonl(data["annotation_path"])
                else:
                    print(f"  Reading JSON file...")
                    annotations = json.load(open(data["annotation_path"], "r"))
                print(f"  Loaded {len(annotations)} annotations")
                sampling_rate = data.get("sampling_rate", 1.0)
                if sampling_rate < 1.0:
                    annotations = random.sample(
                        annotations, int(len(annotations) * sampling_rate)
                    )
                    rank0_print(f"sampling {len(annotations)} examples from dataset {data}")
                else:
                    rank0_print(f"dataset name: {data}")
                print(f"  Setting data_path for annotations...")
                for ann in annotations:
                    if isinstance(ann, list):
                        for sub_ann in ann:
                            sub_ann["data_path"] = data["data_path"]
                    else:
                        ann["data_path"] = data["data_path"]
                list_data_dict += annotations
                print(f"  Total annotations so far: {len(list_data_dict)}")
        else:
            # Lazy mode: do not load jsonl contents into memory. Build fast indexes instead.
            print("Using LAZY loading mode")
            is_dist = (dist is not None) and dist.is_available() and dist.is_initialized()
            rank = dist.get_rank() if is_dist else 0
            world_size = dist.get_world_size() if is_dist else 1

            # keep rank0_print consistent
            try:
                global local_rank
                local_rank = rank
            except Exception:
                pass

            tmp_lazy_files_meta = []
            tmp_lazy_prefix_sums = []
            lazy_total = 0
            for idx, data in enumerate(dataset_list):
                file_format = data["annotation_path"].split(".")[-1]
                if file_format != "jsonl":
                    # For JSON files, keep eager behavior even in lazy mode (already handled above if needed)
                    continue

                if rank == 0:
                    print(f"[{idx+1}/{len(dataset_list)}] Indexing dataset: {data['annotation_path']}")
                    print(f"  Scanning JSONL file...")
                    num_lines, chunk_offsets = self._scan_jsonl_file(data["annotation_path"])  # returns (int, List[int])
                    print(f"  Found {num_lines} lines, {len(chunk_offsets)} chunks")
                    sampling_rate = data.get("sampling_rate", 1.0)
                    if sampling_rate < 1.0:
                        # Pre-sample line indices for this file (deterministic across ranks)
                        sample_count = max(1, int(num_lines * sampling_rate))
                        stable = int(hashlib.md5(data["annotation_path"].encode("utf-8")).hexdigest(), 16)
                        rng = random.Random(self._seed ^ stable)
                        sampled_indices = sorted(rng.sample(range(num_lines), sample_count))
                        effective_len = len(sampled_indices)
                    else:
                        sampled_indices = None
                        effective_len = num_lines

                    tmp_lazy_files_meta.append(
                        {
                            "annotation_path": data["annotation_path"],
                            "data_path": data["data_path"],
                            "num_lines": num_lines,
                            "chunk_offsets": chunk_offsets,
                            "sampling_rate": sampling_rate,
                            "sampled_indices": sampled_indices,
                        }
                    )
                    lazy_total += effective_len
                    tmp_lazy_prefix_sums.append(lazy_total)
                    rank0_print(
                        f"[lazy jsonl] indexed {effective_len}/{num_lines} lines, chunks={len(chunk_offsets)} for {data['annotation_path']}"
                    )

            # Synchronize and broadcast the computed indices to all ranks
            if is_dist:
                if rank == 0:
                    payload = [tmp_lazy_files_meta, tmp_lazy_prefix_sums]
                else:
                    payload = [None, None]
                dist.broadcast_object_list(payload, src=0)
                self._lazy_files_meta = payload[0] if payload[0] is not None else []
                self._lazy_prefix_sums = payload[1] if payload[1] is not None else []
            else:
                self._lazy_files_meta = tmp_lazy_files_meta
                self._lazy_prefix_sums = tmp_lazy_prefix_sums


        rank0_print(f"Total training samples: {len(list_data_dict)}")

        # Deterministic shuffle for eager-loaded portion to keep datasets identical across ranks
        if len(list_data_dict) > 0:
            print(f"Shuffling {len(list_data_dict)} eager-loaded samples...")
            random.Random(self._seed).shuffle(list_data_dict)
            print("Shuffle complete")

        rank0_print("Formatting inputs...Skip in lazy mode")
        print("Updating processor pixels...")
        processor = update_processor_pixels(processor, data_args)
        print("Processor update complete")
        self.processor = processor
        self.tokenizer = processor.tokenizer
        self.data_args = data_args
        self.merge_size = getattr(processor.image_processor, "merge_size", 2)
        self.list_data_dict = list_data_dict

        if data_args.data_packing:
            print("Using PACKED item mode")
            self.item_fn = self._get_packed_item
        else:
            print("Using STANDARD item mode")
            self.item_fn = self._get_item

        print(f"Dataset initialized with {len(self)} total samples")
        print("=" * 80)

    def __len__(self):
        if not self.lazy_read_jsonl:
            return len(self.list_data_dict)
        lazy_len = self._lazy_prefix_sums[-1] if len(self._lazy_prefix_sums) > 0 else 0
        return len(self.list_data_dict) + lazy_len

    @property
    def lengths(self):
        # In lazy mode, computing exact lengths would force reading the entire JSONL.
        # Return a placeholder list to avoid eager loading.
        if self.lazy_read_jsonl:
            return [1] * len(self)
        length_list = []
        for sample in self.list_data_dict:
            img_tokens = 128 if "image" in sample else 0
            length_list.append(
                sum(len(conv["value"].split()) for conv in sample["conversations"]) + img_tokens
            )
        return length_list

    @property
    def modality_lengths(self):
        if self.lazy_read_jsonl:
            return [1] * len(self)
        length_list = []
        for sample in self.list_data_dict:
            cur_len = sum(len(conv["value"].split()) for conv in sample["conversations"])
            cur_len = cur_len if ("image" in sample) or ("video" in sample) else -cur_len
            length_list.append(cur_len)
        return length_list

    @property
    def pre_calculated_length(self):
        if self.lazy_read_jsonl:
            return np.array([1] * len(self))
        if len(self.list_data_dict) > 0 and "num_tokens" in self.list_data_dict[0]:
            length_list = [sample["num_tokens"] for sample in self.list_data_dict]
            return np.array(length_list)
        else:
            print("No pre-calculated length available.")
            return np.array([1] * len(self.list_data_dict))

    def __getitem__(self, i) -> Dict[str, torch.Tensor]:
        num_base_retries = 3
        num_final_retries = 30

        # try the current sample first
        for attempt_idx in range(num_base_retries):
            try:
                sources = self._get_sources(i)
                sample = self.item_fn(sources)
                return sample
            except Exception as e:
                # sleep 1s in case it is a cloud disk issue
                print(f"[Try #{attempt_idx}] Failed to fetch sample {i}. Exception:", e)
                time.sleep(1)

        # try other samples, in case it is file corruption issue
        for attempt_idx in range(num_base_retries):
            try:
                next_index = min(i + 1, len(self) - 1)
                sources = self._get_sources(next_index)

                sample = self.item_fn(sources)
                return sample
            except Exception as e:
                # no need to sleep
                print(
                    f"[Try other #{attempt_idx}] Failed to fetch sample {next_index}. Exception:",
                    e,
                )
                pass

        try:
            sources = self._get_sources(i)
            sample = self.item_fn(sources)
            return sample
        except Exception as e:
            raise e

    def _get_sources(self, global_index):
        """Resolve a global index to the corresponding sample(s) in either the eager list or lazy JSONL.

        Returns a list of one dict or a list of dicts when the JSONL line represents a packed group.
        """
        eager_len = len(self.list_data_dict)
        if global_index < eager_len:
            sources = self.list_data_dict[global_index]
            if isinstance(sources, dict):
                return [sources]
            return sources

        # Lazy JSONL domain
        lazy_idx = global_index - eager_len
        if len(self._lazy_prefix_sums) == 0:
            raise IndexError("Index out of range for empty dataset")
        file_idx = bisect_right(self._lazy_prefix_sums, lazy_idx)
        prev_sum = self._lazy_prefix_sums[file_idx - 1] if file_idx > 0 else 0
        local_idx = lazy_idx - prev_sum

        file_meta = self._lazy_files_meta[file_idx]
        # Map local index through sampling if enabled
        if file_meta["sampled_indices"] is not None:
            line_idx = file_meta["sampled_indices"][local_idx]
        else:
            line_idx = local_idx

        chunk_id = line_idx // self.prefetch_size
        chunk = self._get_jsonl_chunk(file_idx, chunk_id)
        obj = chunk[line_idx % self.prefetch_size]

        # Attach data_path consistently with eager path
        if isinstance(obj, list):
            for sub in obj:
                sub["data_path"] = file_meta["data_path"]
        else:
            obj["data_path"] = file_meta["data_path"]

        if isinstance(obj, dict):
            return [obj]
        return obj

    def _scan_jsonl_file(self, path):
        """Scan a JSONL file in binary mode to count lines and record byte offsets at chunk starts.

        Returns (num_lines, chunk_offsets) where chunk_offsets[i] is the byte offset of the first line in chunk i.
        """
        chunk_offsets = []
        num_lines = 0
        last_print = 0
        print_interval = 100000  # Print every 100k lines
        with open(path, "rb") as f:
            while True:
                start_pos = f.tell()
                line = f.readline()
                if not line:
                    break
                if num_lines % self.prefetch_size == 0:
                    chunk_offsets.append(start_pos)
                num_lines += 1
                # Print progress every print_interval lines
                if num_lines - last_print >= print_interval:
                    print(f"    Scanned {num_lines} lines...")
                    last_print = num_lines
        return num_lines, chunk_offsets

    def _get_jsonl_chunk(self, file_idx, chunk_id):
        """Load and cache a chunk of JSONL lines as parsed JSON objects."""
        key = (file_idx, chunk_id)
        if key in self._chunk_cache:
            # Move to end to mark as recently used
            self._chunk_cache.move_to_end(key)
            return self._chunk_cache[key]

        file_meta = self._lazy_files_meta[file_idx]
        start_offset = file_meta["chunk_offsets"][chunk_id]
        items = []
        with open(file_meta["annotation_path"], "rb") as f:
            f.seek(start_offset)
            for _ in range(self.prefetch_size):
                line = f.readline()
                if not line:
                    break
                # Decode as UTF-8 and parse JSON
                item = json.loads(line.decode("utf-8"))
                items.append(item)

        # Evict if over capacity
        self._chunk_cache[key] = items
        if len(self._chunk_cache) > self._max_cached_chunks:
            self._chunk_cache.popitem(last=False)
        return items

    def _get_item(self, sources) -> Dict[str, torch.Tensor]:
        data_dict = preprocess_qwen_visual(
            sources,
            self.processor,
        )

        seq_len = data_dict["input_ids"][0].size(0)

        if "image_grid_thw" in data_dict:
            grid_thw = data_dict.get("image_grid_thw")
            if not isinstance(grid_thw, Sequence):
                grid_thw = [grid_thw]
        else:
            grid_thw = None

        if "video_grid_thw" in data_dict:
            video_grid_thw = data_dict.get("video_grid_thw")
            if not isinstance(video_grid_thw, Sequence):
                video_grid_thw = [video_grid_thw]
            second_per_grid_ts = [
                self.processor.video_processor.temporal_patch_size
                / self.processor.video_processor.fps
            ] * len(video_grid_thw)
        else:
            video_grid_thw = None
            second_per_grid_ts = None

        position_ids, _ = self.get_rope_index(
            self.merge_size,
            data_dict["input_ids"],
            image_grid_thw=torch.cat(grid_thw, dim=0) if grid_thw else None,
            video_grid_thw=(
                torch.cat(video_grid_thw, dim=0) if video_grid_thw else None
            ),
            second_per_grid_ts=second_per_grid_ts if second_per_grid_ts else None,
        )

        data_dict["position_ids"] = position_ids
        data_dict["attention_mask"] = [seq_len]

        text = self.processor.tokenizer.decode(
            data_dict["input_ids"][0], skip_special_tokens=False
        )

        labels = data_dict["labels"][0]
        labels = [
            tid if tid != -100 else self.processor.tokenizer.pad_token_id
            for tid in labels
        ]
        label = self.processor.tokenizer.decode(labels, skip_special_tokens=False)

        return data_dict

    def _get_packed_item(self, sources) -> Dict[str, torch.Tensor]:

        if isinstance(sources, dict):
            if isinstance(source, dict):
                sources = [sources]
            assert len(sources) == 1, "Don't know why it is wrapped to a list"  # FIXME
            return self._get_item(sources)

        if isinstance(sources, list):
            data_list = []
            new_data_dict = {}
            for source in sources:
                if isinstance(source, dict):
                    source = [source]
                assert (
                    len(source) == 1
                ), f"Don't know why it is wrapped to a list.\n {source}"  # FIXME
                data_list.append(self._get_item(source))

            input_ids = torch.cat([d["input_ids"] for d in data_list], dim=1)
            labels = torch.cat([d["labels"] for d in data_list], dim=1)
            position_ids = torch.cat([d["position_ids"] for d in data_list], dim=2)
            attention_mask = [
                d["attention_mask"][0] for d in data_list if "attention_mask" in d
            ]
            new_data_dict = {
                "input_ids": input_ids,
                "labels": labels,
                "position_ids": position_ids,
                "attention_mask": attention_mask if attention_mask else None,
            }

            if any("pixel_values" in d for d in data_list):
                new_data_dict.update(
                    {
                        "pixel_values": torch.cat(
                            [
                                d["pixel_values"]
                                for d in data_list
                                if "pixel_values" in d
                            ],
                            dim=0,
                        ),
                        "image_grid_thw": torch.cat(
                            [
                                d["image_grid_thw"]
                                for d in data_list
                                if "image_grid_thw" in d
                            ],
                            dim=0,
                        ),
                    }
                )

            if any("pixel_values_videos" in d for d in data_list):
                new_data_dict.update(
                    {
                        "pixel_values_videos": torch.cat(
                            [
                                d["pixel_values_videos"]
                                for d in data_list
                                if "pixel_values_videos" in d
                            ],
                            dim=0,
                        ),
                        "video_grid_thw": torch.cat(
                            [
                                d["video_grid_thw"]
                                for d in data_list
                                if "video_grid_thw" in d
                            ],
                            dim=0,
                        ),
                    }
                )
            return new_data_dict


def pad_and_cat(tensor_list):
    max_length = max(tensor.shape[2] for tensor in tensor_list)

    padded_tensors = []
    for tensor in tensor_list:
        pad_length = max_length - tensor.shape[2]
        padded_tensor = torch.nn.functional.pad(tensor, (0, pad_length), "constant", 1)
        padded_tensors.append(padded_tensor)

    stacked_tensor = torch.cat(padded_tensors, dim=1)

    return stacked_tensor


@dataclass
class DataCollatorForSupervisedDataset(object):
    """Collate examples for supervised fine-tuning."""

    tokenizer: transformers.PreTrainedTokenizer

    def __call__(self, instances: Sequence[Dict]) -> Dict[str, torch.Tensor]:
        input_ids, labels, position_ids = tuple(
            [instance[key] for instance in instances]
            for key in ("input_ids", "labels", "position_ids")
        )
        input_ids = [ids.squeeze(0) for ids in input_ids]
        labels = [ids.squeeze(0) for ids in labels]
        input_ids = torch.nn.utils.rnn.pad_sequence(
            input_ids, batch_first=True, padding_value=self.tokenizer.pad_token_id
        )
        labels = torch.nn.utils.rnn.pad_sequence(
            labels, batch_first=True, padding_value=IGNORE_INDEX
        )
        position_ids = pad_and_cat(position_ids)
        input_ids = input_ids[:, : self.tokenizer.model_max_length]
        labels = labels[:, : self.tokenizer.model_max_length]
        position_ids = position_ids[:, :, : self.tokenizer.model_max_length]
        batch = dict(
            input_ids=input_ids,
            labels=labels,
            attention_mask=input_ids.ne(self.tokenizer.pad_token_id),
        )
        images = list(
            instance["pixel_values"]
            for instance in instances
            if "pixel_values" in instance
        )
        videos = list(
            instance["pixel_values_videos"]
            for instance in instances
            if "pixel_values_videos" in instance
        )
        if len(images) != 0:
            concat_images = torch.cat([image for image in images], dim=0)
            grid_thw = [
                instance["image_grid_thw"]
                for instance in instances
                if "image_grid_thw" in instance
            ]
            grid_thw = torch.cat(grid_thw, dim=0)
        else:
            concat_images = None
            grid_thw = None

        if len(videos) != 0:
            concat_videos = torch.cat([video for video in videos], dim=0)
            video_grid_thw = [
                instance["video_grid_thw"]
                for instance in instances
                if "video_grid_thw" in instance
            ]
            video_grid_thw = torch.cat(video_grid_thw, dim=0)
        else:
            concat_videos = None
            video_grid_thw = None

        batch["pixel_values"] = concat_images
        batch["image_grid_thw"] = grid_thw
        batch["pixel_values_videos"] = concat_videos
        batch["video_grid_thw"] = video_grid_thw
        batch["position_ids"] = position_ids
        return batch


@dataclass
class FlattenedDataCollatorForSupervisedDataset(DataCollatorForSupervisedDataset):
    """Collate examples into packed sequence with multi-modal support."""

    tokenizer: transformers.PreTrainedTokenizer
    truncate_to_max_length: bool = True
    model_max_length: int = None

    def __call__(self, instances: Sequence[Dict]) -> Dict[str, torch.Tensor]:
        input_ids, labels, position_ids, attention_mask = tuple(
            [instance[key] for instance in instances]
            for key in ("input_ids", "labels", "position_ids", "attention_mask")
        )
        attention_mask = list(
            itertools.chain(
                *(
                    instance["attention_mask"]
                    for instance in instances
                    if "attention_mask" in instance
                )
            )
        )
        seq_lens = torch.tensor([0] + attention_mask, dtype=torch.int32)
        cumsum_seq_lens = torch.cumsum(seq_lens, dim=0, dtype=torch.int32)
        input_ids = torch.cat(input_ids, dim=1)
        labels = torch.cat(labels, dim=1)
        position_ids = torch.cat(position_ids, dim=2)

        # Truncate to model_max_length if enabled
        num_sequences_to_keep = len(instances)  # Track how many sequences we keep

        # check number of image tokens for each instance
        
        for instance in instances:
            # print("input ids size: ", instance["input_ids"].size())
            num_image_tokens = (instance["input_ids"] == IMAGE_TOKEN_INDEX).sum().item()
            # print(f"Number of image tokens for instance: {num_image_tokens}")
        
        if self.truncate_to_max_length:
            # Use model_max_length from args, fallback to tokenizer's if not provided
            max_length = self.model_max_length if self.model_max_length is not None else self.tokenizer.model_max_length
            if input_ids.shape[1] > max_length:
                print(f"Truncating from {input_ids.shape[1]} to {max_length}")
                mask = cumsum_seq_lens <= max_length
                cumsum_seq_lens_filtered = cumsum_seq_lens[mask]

                # Check if we have at least 2 elements (start + at least one end boundary)
                if len(cumsum_seq_lens_filtered) < 2:
                    print(f"WARNING: First sequence length ({cumsum_seq_lens[1].item() if len(cumsum_seq_lens) > 1 else 'N/A'}) exceeds max_length ({max_length}). Truncating first sequence to max_length.")
                    # Truncate the first sequence to max_length
                    last_index = max_length
                    cumsum_seq_lens = torch.tensor([0, max_length], dtype=torch.int32)  # [start, end]
                    num_sequences_to_keep = 1
                else:
                    print("Truncating sequence that has more than 2 cumsum_seq_lens_filtered")
                    # Keep complete sequences that fit within max_length
                    # cumsum_seq_lens_filtered has boundaries up to and including those <= max_length
                    # The last element is a boundary that's <= max_length, so we use it
                    last_index = cumsum_seq_lens_filtered[-1].item()  # Get the last boundary value

                    # For packed sequences, we need to keep: [0, end_seq1, end_seq2, ..., end_last_complete_seq]
                    # But NOT the boundary that would start the next (truncated) sequence
                    # cumsum_seq_lens_filtered already contains only boundaries <= max_length
                    # So we keep all of them
                    cumsum_seq_lens = cumsum_seq_lens_filtered

                    # Calculate how many sequences we're keeping
                    # Number of sequences = number of boundaries - 1 (excluding the starting 0)
                    num_sequences_to_keep = len(cumsum_seq_lens) - 1

                print(f"Keeping {num_sequences_to_keep} out of {len(instances)} sequences, truncating to {last_index} tokens")

                # Only truncate if we're keeping at least one sequence
                # Truncate image/video counts to match kept sequences
                input_ids = input_ids[:, :last_index]
                labels = labels[:, :last_index]
                position_ids = position_ids[:, :, :last_index]

        batch = dict(
            input_ids=input_ids,
            labels=labels,
            attention_mask=cumsum_seq_lens,
            position_ids=position_ids,
        )

        # Only include images/videos from sequences we're keeping
        instances_to_use = instances[:num_sequences_to_keep]

        images = list(
            instance["pixel_values"]
            for instance in instances_to_use
            if "pixel_values" in instance
        )
        videos = list(
            instance["pixel_values_videos"]
            for instance in instances_to_use
            if "pixel_values_videos" in instance
        )

        if len(images) != 0:
            concat_images = torch.cat([image for image in images], dim=0)
            grid_thw = [
                instance["image_grid_thw"]
                for instance in instances_to_use
                if "image_grid_thw" in instance
            ]
            grid_thw = torch.cat(grid_thw, dim=0)

        else:
            concat_images = None
            grid_thw = None

        if len(videos) != 0:
            concat_videos = torch.cat([video for video in videos], dim=0)
            video_grid_thw = [
                instance["video_grid_thw"]
                for instance in instances_to_use
                if "video_grid_thw" in instance
            ]
            video_grid_thw = torch.cat(video_grid_thw, dim=0)

        else:
            concat_videos = None
            video_grid_thw = None

        batch["pixel_values"] = concat_images
        batch["image_grid_thw"] = grid_thw
        batch["pixel_values_videos"] = concat_videos
        batch["video_grid_thw"] = video_grid_thw

        return batch


def make_supervised_data_module(processor, data_args, model_max_length) -> Dict:
    """Make dataset and collator for supervised fine-tuning."""
    print("Creating supervised dataset...")
    train_dataset = LazySupervisedDataset(processor, data_args=data_args)
    print(f"Dataset created with {len(train_dataset)} samples")

    if data_args.data_flatten or data_args.data_packing:
        print("Creating flattened data collator...")
        data_collator = FlattenedDataCollatorForSupervisedDataset(processor.tokenizer, truncate_to_max_length=data_args.truncate_to_max_length, model_max_length=model_max_length)
        print("Flattened data collator created")
        return dict(
            train_dataset=train_dataset, eval_dataset=None, data_collator=data_collator
        )
    print("Creating standard data collator...")
    data_collator = DataCollatorForSupervisedDataset(processor.tokenizer)
    print("Standard data collator created")
    return dict(
        train_dataset=train_dataset, eval_dataset=None, data_collator=data_collator
    )


if __name__ == "__main__":
    pass
