from dataclasses import dataclass

@dataclass
class QuantConfig:
    """
    Configurations for model compression levels.
    """
    bit_width: int = 4  # Default to 4-bit for best balance of speed/quality
    group_size: int = 128
    precision: str = "int4" # int4, int8, float16
    method: str = "awq" # awq, gptq, gguf
