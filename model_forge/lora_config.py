from dataclasses import dataclass
from typing import Optional

@dataclass
class ForgeConfig:
    """
    Hyperparameter orchestration for custom SLM/LLM training.
    """
    model_name_or_path: str
    dataset_path: str
    output_dir: str = "./outputs"
    learning_rate: float = 2e-4
    batch_size: int = 4
    gradient_accumulation_steps: int = 4
    num_train_epochs: int = 3
    max_seq_length: int = 2048
    lora_rank: int = 16
    lora_alpha: int = 32
    lora_dropout: float = 0.05
    target_modules: Optional[list] = None 
    # Defaults to common attention blocks if not specified
