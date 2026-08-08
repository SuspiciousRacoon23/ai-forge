import os
import subprocess

class OptimiserXExporter:
    """
    Handles the packaging of models for client delivery.
    """
    def __init__(self, model_dir: str):
        self.model_dir = model_dir

    def package_for_ollama(self, modelfile_content: str):
        """
        Creates a Modelfile for seamless Ollama deployment.
        """
        modelfile_path = os.path.join(self.model_dir, "Modelfile")
        with open(modelfile_path, "w") as f:
            f.write(modelfile_content)
        
        return modelfile_path

    def run_shell_conversion(self, command: str):
        """
        Executes external conversion tools (e.g. llama.cpp's convert-hf-to-gguf.py)
        """
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        if result.returncode != 0:
            raise RuntimeError(f"Conversion failed: {result.stderr}")
        return result.stdout
