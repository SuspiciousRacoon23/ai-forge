import os
from typing import List, Dict, Any
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from .engine import InferenceEngine
from .rag_bridge import RAGBridge

class QueryRequest(BaseModel):
    query: str
    context_id: str = None
    stream: bool = False

class QueryResponse(BaseModel):
    answer: str
    sources: List[str] = []
    latency: float = 0.0

app = FastAPI(title="Nexus-Serve API")
engine = InferenceEngine()
rag = RAGBridge()

@app.post("/generate", response_model=QueryResponse)
async def generate(request: QueryRequest):
    """
    The primary entry point for client model interaction.
    Integrates RAG grounding before model inference.
    """
    # 1. Grounding: Fetch relevant context from the RAG bridge
    context = ""
    sources = []
    if request.context_id:
        context, sources = rag.retrieve(request.query, request.context_id)
    
    # 2. Augmentation: Construct the final prompt
    augmented_prompt = f"Context: {context}\n\nQuery: {request.query}" if context else request.query
    
    # 3. Inference: Pass to the high-performance engine
    answer, latency = engine.predict(augmented_prompt)
    
    return QueryResponse(
        answer=answer,
        sources=sources,
        latency=latency
    )
