import os
import sys

# The "Godmode" path fix: Explicitly add the forge root to the path
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(ROOT_DIR)

import os
import sys

# The "Godmode" path fix: Explicitly add the forge root to the path
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(ROOT_DIR)

# Using hyphenated directory names as modules (requiring manual import since Python doesn't like hyphens in names)
# We will import from the directory structure explicitly.
import os
import sys

# The "Godmode" path fix: Explicitly add the forge root to the path
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(ROOT_DIR)

from model_forge.trainer import ModelForge
from model_forge.lora_config import ForgeConfig
from datasets import load_dataset
from optimiser_x.quantizer import OptimiserXQuantizer
from optimiser_x.quantization_config import QuantConfig


def execute_sovereign_training():
    print("🚀 INITIALIZING SUPREME GODMODE TRAINING: RUN_001_SOVEREIGN")
    
    # 1. Configuration for a "King" Model: High Rank, Deep Adaptation
    config = ForgeConfig(
        model_name_or_path="Qwen/Qwen2.5-1.5B-Instruct", # Start with elite SLM
        dataset_path="Code/BxT Labs/AI-Forge/datasets/synthetic_industrial/sovereign_core.jsonl",
        output_dir="Code/BxT Labs/AI-Forge/training_runs/run_001_sovereign",
        learning_rate=1e-4,
        num_train_epochs=5, # Iterative refinement for "King" status
        lora_rank=64,       # High rank for deeper conceptual absorption
        lora_alpha=128,
        batch_size=2,
        gradient_accumulation_steps=8
    )
    
    forge = ModelForge(config)
    
    # 2. Heat the Forge: SFT/QLoRA
    print("🔥 Heating the Forge... Absorbing industrial sovereignty...")
    dataset = load_dataset("json", data_files=config.dataset_path, split="train")
    forge.train(dataset)
    
    # 3. Crystallize: Quantization for absolute efficiency
    print("💎 Crystallizing weights into 4-bit AWQ...")
    q_config = QuantConfig(bit_width=4, method="awq")
    quantizer = OptimiserXQuantizer(config.output_dir, q_config)
    quant_path = quantizer.apply_awq(calibration_data=[]) # Simulation of calibration
    
    print(f"👑 THE KING HAS RISEN. Model deployed at: {quant_path}")

if __name__ == "__main__":
    execute_sovereign_training()
