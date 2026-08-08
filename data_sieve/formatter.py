import json
from typing import List, Dict

class DataSieveFormatter:
    """
    Converts cleaned data into Instruction-Tuning formats.
    Targets: Llama-3, Qwen, and Phi style prompts.
    """
    def __init__(self, format_type: str = "chatml"):
        self.format_type = format_type

    def to_instruction_pair(self, context: str, question: str, answer: str) -> Dict:
        """
        Creates a structured training sample.
        """
        if self.format_type == "chatml":
            # ChatML format used by Qwen and many SLMs
            return {
                "messages": [
                    {"role": "system", "content": "You are a specialized industrial intelligence assistant."},
                    {"role": "user", "content": f"Context: {context}\n\nQuestion: {question}"},
                    {"role": "assistant", "content": answer}
                ]
            }
        else:
            # Standard Alpaca format
            return {
                "instruction": question,
                "input": context,
                "output": answer
            }

    def save_dataset(self, samples: List[Dict], output_path: str):
        with open(output_path, "w", encoding="utf-8") as f:
            for sample in samples:
                f.write(json.dumps(sample) + "\n")
