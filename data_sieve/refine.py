import re
from typing import List, Dict

class DataSieveRefiner:
    """
    Cleaning and noise reduction.
    Focuses on industrial technicalities and PII removal.
    """
    def __init__(self, pii_patterns: List[str] = None):
        self.pii_patterns = pii_patterns or [
            r"\b[A-Za-z0-9_.+-]+@[A-Za-z0-9-]+\.[A-Za-z0-9-.]+\b", # Email
            r"\b\d{3}-\d{3}-\d{4}\b", # Phone (Generic)
            r"Order ID: \w+", # Client Specific PII
        ]

    def clean_text(self, text: str) -> str:
        # Remove excessive whitespace
        text = re.sub(r'\s+', ' ', text).strip()
        
        # Scrub PII
        for pattern in self.pii_patterns:
            text = re.sub(pattern, "[REDACTED]", text)
            
        # Remove common PDF artifacts (e.g., "Page X of Y")
        text = re.sub(r"Page \d+ of \d+", "", text)
        
        return text

    def chunk_text(self, text: str, max_tokens: int = 512) -> List[str]:
        # Simple character-based chunking for now, ideally token-based
        words = text.split()
        chunks = []
        current_chunk = []
        
        for word in words:
            if len(current_chunk) < max_tokens:
                current_chunk.append(word)
            else:
                chunks.append(" ".join(current_chunk))
                current_chunk = [word]
        
        if current_chunk:
            chunks.append(" ".join(current_chunk))
            
        return chunks
