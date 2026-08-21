# AI Service - FastAPI Adapter

This is a Python 3.10+ service utilizing FastAPI to perform answer evaluations and generate adaptive technical questions.

## Project Structure

- `app/main.py`: Entrypoint initializing routes.
- `app/routes/`: Router implementations for starting, evaluation, and adaptive question fetching.
- `app/services/`: Evaluation grading calculations, adaptive algorithms, and LLM communication handlers.
- `app/models/`: Pydantic input/output validation schemas and prompt templates.
- `app/rag/`: Scaffolding for embedding creation, vector stores, and content retrieval.
- `datasets/`: Storage of local sample questions, answers, and training files.
- `training/`: Scaffolding scripts for dataset formatting and model fine-tuning.

---

## Local Setup

1. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/Scripts/activate # On Windows: venv\Scripts\activate
   ```
2. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the development server:
   ```bash
   uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload
   ```
