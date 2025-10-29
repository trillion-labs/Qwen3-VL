# Adopted from https://github.com/lm-sys/FastChat. Below is the original copyright:
# Adopted from tatsu-lab@stanford_alpaca. Below is the original copyright:
#    Copyright 2023 Rohan Taori, Ishaan Gulrajani, Tianyi Zhang, Yann Dubois, Xuechen Li
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

import os
import logging
import pathlib
import torch
import transformers
import sys
from pathlib import Path

project_root = Path(__file__).parent.parent.parent
sys.path.append(str(project_root))

from trainer import replace_qwen2_vl_attention_class

from transformers import (
    Qwen2VLForConditionalGeneration,
    Qwen2_5_VLForConditionalGeneration,
    Qwen3VLForConditionalGeneration,
    Qwen3VLMoeForConditionalGeneration
)
from qwenvl.model.qwen2_5_vl import Qwen2_5_VLForConditionalGenerationWithDummy
from qwenvl.data.data_processor import make_supervised_data_module
from qwenvl.train.argument import (
    ModelArguments,
    DataArguments,
    TrainingArguments,
)
from transformers import AutoProcessor, Trainer

local_rank = None


def rank0_print(*args):
    if local_rank == 0:
        print(*args)


def safe_save_model_for_hf_trainer(trainer: transformers.Trainer, output_dir: str):
    """Collects the state dict and dump to disk."""

    if trainer.deepspeed:
        torch.cuda.synchronize()
        trainer.save_model(output_dir)
        return

    state_dict = trainer.model.state_dict()
    if trainer.args.should_save:
        cpu_state_dict = {key: value.cpu() for key, value in state_dict.items()}
        del state_dict
        trainer._save(output_dir, state_dict=cpu_state_dict)  # noqa


def set_model(model_args, model):
    if model_args.tune_mm_vision:
        for n, p in model.visual.named_parameters():
            p.requires_grad = True
    else:
        for n, p in model.visual.named_parameters():
            p.requires_grad = False

    if model_args.tune_mm_mlp:
        for n, p in model.visual.merger.named_parameters():
            p.requires_grad = True
    else:
        for n, p in model.visual.merger.named_parameters():
            p.requires_grad = False

    if model_args.tune_mm_llm:
        for n, p in model.language_model.named_parameters():
            p.requires_grad = True
        model.lm_head.requires_grad = True
    else:
        for n, p in model.language_model.named_parameters():
            p.requires_grad = False
        model.lm_head.requires_grad = False


def train(attn_implementation="flash_attention_2"):
    global local_rank

    print("=" * 80)
    print("STARTING TRAIN FUNCTION")
    print("=" * 80)

    print("Parsing arguments...")
    parser = transformers.HfArgumentParser(
        (ModelArguments, DataArguments, TrainingArguments)
    )
    model_args, data_args, training_args = parser.parse_args_into_dataclasses()
    print("Arguments parsed successfully")

    local_rank = training_args.local_rank
    os.makedirs(training_args.output_dir, exist_ok=True)

    print(f"Local rank: {local_rank}")
    print(f"Output directory: {training_args.output_dir}")
    print(f"Loading model from: {model_args.model_name_or_path}")

    if "qwen3" in model_args.model_name_or_path.lower() and "a" in Path(model_args.model_name_or_path.rstrip("/")).name.lower():
        print("Detected Qwen3VL MoE model - loading...")
        model = Qwen3VLMoeForConditionalGeneration.from_pretrained(
            model_args.model_name_or_path,
            cache_dir=training_args.cache_dir,
            attn_implementation=attn_implementation,
            dtype=(torch.bfloat16 if training_args.bf16 else None),
        )
        data_args.model_type = "qwen3vl"
        print("Qwen3VL MoE model loaded successfully")
    elif "qwen3" in model_args.model_name_or_path.lower():
        print("Detected Qwen3VL model - loading...")
        model = Qwen3VLForConditionalGeneration.from_pretrained(
            model_args.model_name_or_path,
            cache_dir=training_args.cache_dir,
            attn_implementation=attn_implementation,
            dtype=(torch.bfloat16 if training_args.bf16 else None),
        )
        data_args.model_type = "qwen3vl"
        print("Qwen3VL model loaded successfully")
    elif "qwen2.5" in model_args.model_name_or_path.lower():
        print("Detected Qwen2.5VL model - loading...")
        if model_args.use_dummy_handler:
            print("Using dummy handler version")
            model = Qwen2_5_VLForConditionalGenerationWithDummy.from_pretrained(
                model_args.model_name_or_path,
                cache_dir=training_args.cache_dir,
                attn_implementation=attn_implementation,
                dtype=(torch.bfloat16 if training_args.bf16 else None),
            )
        else:
            print("Using standard version")
            model = Qwen2_5_VLForConditionalGeneration.from_pretrained(
                model_args.model_name_or_path,
                cache_dir=training_args.cache_dir,
                attn_implementation=attn_implementation,
                dtype=(torch.bfloat16 if training_args.bf16 else None),
            )
        data_args.model_type = "qwen2.5vl"
        print("Qwen2.5VL model loaded successfully")
    else:
        print("Detected Qwen2VL model - loading...")
        model = Qwen2VLForConditionalGeneration.from_pretrained(
            model_args.model_name_or_path,
            cache_dir=training_args.cache_dir,
            attn_implementation=attn_implementation,
            dtype=(torch.bfloat16 if training_args.bf16 else None),
        )
        data_args.model_type = "qwen2vl"
        print("Qwen2VL model loaded successfully")

    print(f'the initlized model is {model_args.model_name_or_path} the class is {model.__class__.__name__}')
    print("Loading processor...")
    processor = AutoProcessor.from_pretrained(
        model_args.model_name_or_path,
    )
    print("Processor loaded successfully")

    if data_args.data_flatten or data_args.data_packing:
        print("Replacing attention class for flatten/packing mode...")
        replace_qwen2_vl_attention_class()
        print("Attention class replaced")
    model.config.use_cache = False
    print("Model cache disabled")

    if training_args.gradient_checkpointing:
        print("Setting up gradient checkpointing...")
        if hasattr(model, "enable_input_require_grads"):
            model.enable_input_require_grads()
        else:

            def make_inputs_require_grad(module, input, output):
                output.requires_grad_(True)

            model.get_input_embeddings().register_forward_hook(make_inputs_require_grad)
        print("Gradient checkpointing setup complete")

    print("Loading tokenizer...")
    tokenizer = transformers.AutoTokenizer.from_pretrained(
        model_args.model_name_or_path,
        cache_dir=training_args.cache_dir,
        model_max_length=training_args.model_max_length,
        padding_side="right",
        use_fast=False,
    )
    print("Tokenizer loaded successfully")
    print("Setting model parameters (freezing/unfreezing layers)...")
    set_model(model_args, model)
    print("Model parameters set")

    if torch.distributed.get_rank() == 0:
        print("=" * 80)
        print("TRAINABLE PARAMETERS SUMMARY")
        print("=" * 80)
        model.visual.print_trainable_parameters()
        model.model.print_trainable_parameters()

    print("=" * 80)
    print("CREATING DATA MODULE")
    print("=" * 80)
    data_module = make_supervised_data_module(processor, data_args=data_args, model_max_length=training_args.model_max_length)
    print("Data module created successfully")

    print("=" * 80)
    print("INITIALIZING TRAINER")
    print("=" * 80)
    trainer = Trainer(
        model=model, processing_class=tokenizer, args=training_args, **data_module
    )
    print("Trainer initialized successfully")

    print("=" * 80)
    print("STARTING TRAINING")
    print("=" * 80)
    if list(pathlib.Path(training_args.output_dir).glob("checkpoint-*")):
        logging.info("checkpoint found, resume training")
        print("Resuming from checkpoint...")
        trainer.train(resume_from_checkpoint=True)
    else:
        print("Starting training from scratch...")
        trainer.train()
    print("Training completed!")

    print("Saving trainer state...")
    trainer.save_state()
    print("Trainer state saved")

    model.config.use_cache = True

    print("Saving model...")
    safe_save_model_for_hf_trainer(trainer=trainer, output_dir=training_args.output_dir)
    print("Model saved")

    print("Saving processor...")
    processor.save_pretrained(training_args.output_dir)
    print("Processor saved")
    print("=" * 80)
    print("TRAINING COMPLETE!")
    print("=" * 80)


if __name__ == "__main__":
    train(attn_implementation="flash_attention_2")
