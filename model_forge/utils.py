import torch
from transformers import AutoTokenizer

def tokenize_function(examples, tokenizer, max_length=2048):
    """
    Standardizes tokenization for training batches.
    """
    # This assumes ChatML style input: {"messages": [{"role": "user", "content": "..."}, ...]}
    texts = []
    for msg_list in examples["messages"]:
        full_text = ""
        for msg in msg_list:
            full_text += f"<{msg['role']}>{msg['content']}\n"
        texts.append(full_text)
    
    return tokenizer(
        texts,
        truncation=True,
        max_length=max_length,
        padding="max_length"
    )

def merge_lora_weights(base_model_path: str, lora_adapter_path: str, output_path: str):
    """
    Collapses LoRA weights back into the base model for production.
    """
    from peft import PeftModel
    from transformers import AutoModelForCausalLM

    base_model = AutoModelForCausalLM.from_pretrained(base_model_path, torch_dtype=torch.float16, device_map="cpu")
    model = PeftModel.from_pretrained(base_model, lora_adapter_path)
    merged_model = model.merge_and_unload()
    merged_model.save_pretrained(output_path)
