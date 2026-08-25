import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

# Load environmental configs
load_dotenv()

from app.routes import interview, question, evaluation, final_report

app = FastAPI(
    title="Coordinated AI Interview Panel API",
    description="Python FastAPI Adapter backend for evaluations and question adaptivity.",
    version="0.1.0"
)

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Attach Routers
app.include_router(interview.router)
app.include_router(question.router)
app.include_router(evaluation.router)
app.include_router(final_report.router)

@app.get("/")
def root():
    return {
        "service": "Coordinated AI Interview Panel - AI Service",
        "status": "active",
        "docs": "/docs"
    }

if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8000))
    uvicorn.run("app.main:app", host="127.0.0.1", port=port, reload=True)
