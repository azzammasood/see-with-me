from fastapi import FastAPI
from database.postgres import get_db
from database.pinecone_db import query_vector
from ml.cloud_llm import generate_response

app = FastAPI(title="See With Me API", version="0.1.0")

@app.get("/")
def read_root():
    return {"message": "See With Me Backend API is running."}

@app.get("/api/health")
def health_check():
    return {"status": "healthy"}

@app.post("/api/vqa")
def visual_question_answering(query: str, image_b64: str = None):
    # This acts as a stub to show architecture.
    # 1. Edge ML (Yolo) would have cropped/passed images here.
    # 2. Could query pinecone here for context.
    # 3. Cloud LLM processes prompt.
    context = query_vector(query)
    response = generate_response(query, context, image_b64)
    return {"response": response}

