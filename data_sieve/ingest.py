import os
import re
from typing import List, Dict
import PyPDF2 # Assuming this is available or needs to be added to requirements

class DataSieveIngestor:
    """
    Handles high-volume ingestion of raw files.
    Supports PDF, TXT, and Email-like formats.
    """
    def __init__(self, input_dir: str):
        self.input_dir = input_dir

    def extract_text_from_pdf(self, pdf_path: str) -> str:
        text = ""
        with open(pdf_path, "rb") as f:
            reader = PyPDF2.PdfReader(f)
            for page in reader.pages:
                text += page.extract_text() + "\n"
        return text

    def extract_text_from_txt(self, txt_path: str) -> str:
        with open(txt_path, "r", encoding="utf-8") as f:
            return f.read()

    def scan_directory(self) -> List[Dict]:
        documents = []
        for root, _, files in os.walk(self.input_dir):
            for file in files:
                path = os.path.join(root, file)
                if file.endswith(".pdf"):
                    documents.append({"source": path, "content": self.extract_text_from_pdf(path)})
                elif file.endswith(".txt"):
                    documents.append({"source": path, "content": self.extract_text_from_txt(path)})
        return documents

# Example Usage’
if __name__ == "__main__":
    ingestor = DataSieveIngestor("./raw_data")
    print(f"Sieving documents from {ingestor.input_dir}...")
    # docs = ingestor.scan_directory()
