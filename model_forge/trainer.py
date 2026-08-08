import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, TrainingArguments, Trainer, TrainerCallback
from peft import LoraConfig, get_peft_model, prepare_model_for_kbit_training
from datasets import load_dataset
from .lora_config import ForgeConfig

class ModelForge:
    """
    The Core Engine for SFT and QLoRA.
    Transforms base models into domain experts.
    """
    def __init__(self, config: ForgeConfig):
        self.config = config
        self.tokenizer = AutoTokenizer.from_pretrained(config.model_name_or_path)
        self.tokenizer.pad_token = self.tokenizer.eos_token
        
    def prepare_model(self, use_qlora: bool = True):
        """
        Weights the model for the forge.
        """
        if use_qlora:
            # Load 4-bit for efficiency
            model = AutoModelForCausalLM.from_pretrained(
                self.config.model_name_or_path,
                load_in_4bit=True,
                torch_dtype=torch.bfloat16,
                device_map="auto"
            )
            model = prepare_model_for_kbit_training(model)
        else:
            model = AutoModelForCausalLM.from_pretrained(
                self.config.model_name_or_path,
                torch_dtype=torch.bfloat16,
                device_map="auto"
            )

        # Apply LoRA (Low-Rank Adaptation)
        lora_config = LoraConfig(
            r=self.config.lora_rank,
            lora_alpha=self.config.lora_alpha,
            target_modules=self.config.target_modules or ["q_proj", "v_proj", "k_proj", "o_proj"],
            lora_dropout=self.config.lora_dropout,
            bias="none",
            task_type="CAUSAL_LM"
        )
        
        return get_peft_model(model, lora_config)

    def train(self, train_dataset):
        """
        The actual heating process.
        """
        model = self.prepare_model()
        
        training_args = TrainingArguments(
            output_dir=self.config.output_dir,
            per_device_train_batch_size=self.config.batch_size,
            gradient_accumulation_steps=self.config.gradient_accumulation_steps,
            learning_rate=self.config.learning_rate,
            num_train_epochs=self.config.num_train_epochs,
            logging_steps=10,
            optim="paged_adamw_32bit",
            save_strategy="epoch",
            bf16=True, # Use bfloat16 for Ampere+ GPUs
            push_to_hub=False,
            report_to="none" # can be set to "wandb"
        )

        trainer = Trainer(
            model=model,
            args=training_args,
            train_dataset=train_dataset,
            # data_collator=... (would be defined in utils)
        )
        
        trainer.train()
        model.save_pretrained(self.config.output_dir)
        self.tokenizer.save_pretrained(self.config.output_dir)
        print(f"Model forged successfully at {self.config.output_dir}")
