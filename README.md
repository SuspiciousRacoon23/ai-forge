> ⚠️ **STATUS (2026-06-13): RESEARCH SPIKE — NOT A PRODUCT.**
> The core inference path is a hardcoded `[simulated response]` mock. It has never run end-to-end, and its integration shapes with SoftSol do not match at runtime (the wiring would fail if called). Everything below describes the *intended* foundry, not what exists. **Do not put AI-Forge in any investor or strategy framing as a working capability.** If SoftSol ever needs AI, a hosted API (Claude/OpenAI) is the build-vs-buy default and removes nearly all the ML maintenance burden. See decision F2 in `/NOW.md`.

# AI-Forge: The LLM/SLM Foundry

## 🌌 The Vision
AI-Forge is not just a set of scripts; it is a precision-engineered pipeline to transform raw industrial data into elite, specialized intelligence. We move from "General Knowledge" to "Domain Sovereignty."

## ⚙️ System Architecture (The Forge)

### 1. Data-Sieve (The Refiner)
*Objective: Pure, high-density training data.*
- **Ingest**: PDF, HTML, Email, DB logs.
- **Sift**: De-duplication, PII removal, noise filtration.
- **Amplify**: LLM-powered synthetic data expansion (Self-Instruct).
- **Format**: Instruction-Tuning JSONL mapping.

### 2. Model-Forge (The Core)
*Objective: High-fidelity model alignment.*
- **Base Selection**: SLMs (Phi, Qwen) vs LLMs (Llama, Mistral).
- **Fine-Tuning**: SFT $\rightarrow$ QLoRA $\rightarrow$ DPO.
- **Control**: Hyperparameter orchestration via YAML configs.

### 3. Optimiser-X (The Compressor)
*Objective: Maximum performance, minimum footprint.*
- **Precision**: 4-bit/8-bit Quantization.
- **Formats**: GGUF (CPU/Local), AWQ (GPU), EXL2.
- **Slicing**: Layer pruning and distillation.

### 4. Nexus-Serve (The Interface)
*Objective: Seamless client delivery.*
- **Engine**: vLLM / Ollama.
- **Grounding**: Hybrid RAG (Vector + Graph).
- **Feedback**: Real-time human-in-the-loop evaluation traces.

## 🚀 Execution Roadmap
1. `[ ]` **Sieve-Alpha**: PDF $\rightarrow$ JSONL pipeline.
2. `[ ]` **Forge-Alpha**: LoRA training script for Qwen-0.5B.
3. `[ ]` **Opti-Alpha**: GGUF export workflow.
4. `[ ]` **Nexus-Alpha**: API endpoint with RAG integration.

---

**Connected:** vault planning note: [Custom_LLM_SLM_Planning](../../../BxT%20Labs/imp/02_PRODUCT/Custom_LLM_SLM_Planning.md)
