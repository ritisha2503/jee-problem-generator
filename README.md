# 🎓 MathGen-RAG: Advanced JEE Math Problem Synthesizer

An intelligent, production-ready Retrieval-Augmented Generation (RAG) platform tailored for competitive mathematics education. Standard textbooks often suffer from repetitive Past Year Questions (PYQs). **MathGen-RAG** solves this by ingestion-indexing complex mathematical PDFs, parsing intricate LaTeX formulas seamlessly, and prompting state-of-the-art LLMs to generate entirely original, conceptual, and highly challenging JEE Advanced-level problems paired with step-by-step solutions.

## ✨ Key Features

*   **⚡ Modern Python Stack:** Initialized and managed via `uv` for blazing-fast, deterministic dependency handling.
*   **📐 LaTeX-Optimized Chunking:** Custom-configured LangChain `RecursiveCharacterTextSplitter` that protects mathematical syntax (`$$`, `\[`, `\begin{equation}`) from breaking during vector ingestion.
*   **🧠 Multi-Model Playground:** Dynamic UI-driven routing to evaluate and compare top-tier models: **Kimi K2.6**, **Qwen**, and **Gemini Flash-Lite**.
*   **📁 Robust Data Pipeline:** Automatic extraction via LangChain's `PyPDFLoader`, paired with local/cloud Hugging Face embedding pipelines and highly accurate vector storage.
*   **🎨 Intuitive Control Panel:** A lightweight UI powered by FastAPI to index your local `src/` directory, select your model configuration, and review rendered Markdown/LaTeX outputs instantly.