import time
from fastapi import FastAPI, Depends, HTTPException, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List

from database.postgres import get_db, init_db
from database.schemas import VQARequest, VQAResponse, UserSchema, ActivitySchema
from database.pinecone_db import vector_store
from ml.cloud_llm import ai_service
from ml.yolo_edge import vision_handler

app = FastAPI(
    title="See With Me - Production Core API",
    description="Backend services for real-time voice-native mobility assistance.",
    version="1.0.0"
)

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # In production, restrict to specific domains
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def startup_event():
    # Initialize database tables on startup
    # init_db() # Uncomment when DATABASE_URL is active
    pass

@app.get("/")
async def root():
    return {
        "status": "online",
        "service": "See With Me API",
        "timestamp": time.time()
    }

@app.post("/api/v1/analyze", response_model=VQAResponse)
async def analyze_environment(request: VQARequest):
    start_time = time.time()
    
    # 1. Retrieve Context from Spatial Memory
    context = vector_store.query_spatial_memory(request.query)
    
    # 2. Process with Multimodal AI
    response_text = await ai_service.process_multimodal_query(
        prompt=request.query,
        image_data=request.image_b64
    )
    
    latency = (time.time() - start_time) * 1000
    
    return VQAResponse(
        response=response_text,
        context=context,
        latency_ms=latency
    )

@app.post("/api/v1/edge/hazards")
async def check_hazards(detections: List[dict]):
    """Endpoint for zero-latency safety verification from client-side YOLO."""
    return vision_handler.process_edge_trigger(detections)

@app.get("/api/v1/user/activities", response_model=List[ActivitySchema])
async def get_activities(db: Session = Depends(get_db)):
    # This would normally query the DB. 
    # For Git demo purposes, we return a structured response that matches the schema.
    return [
        {"id": 1, "label": "Went for walking", "timestamp_str": "SUN, 12:00 AM", "user_id": 1, "created_at": "2024-04-19T12:00:00"},
        {"id": 2, "label": "Read text", "timestamp_str": "SAT, 3:00 PM", "user_id": 1, "created_at": "2024-04-18T15:00:00"},
    ]
