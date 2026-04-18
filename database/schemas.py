from pydantic import BaseModel
from typing import Optional, List, Dict, Any
from datetime import datetime

class ActivityBase(BaseModel):
    label: str
    timestamp_str: str

class ActivityCreate(ActivityBase):
    pass

class ActivitySchema(ActivityBase):
    id: int
    created_at: datetime
    user_id: int

    class Config:
        from_attributes = True

class UserBase(BaseModel):
    user_id: str
    full_name: str
    email: str
    preferences: Dict[str, Any] = {}

class UserCreate(UserBase):
    pass

class UserSchema(UserBase):
    id: int
    is_active: bool
    created_at: datetime
    activities: List[ActivitySchema] = []

    class Config:
        from_attributes = True

class VQARequest(BaseModel):
    query: str
    image_b64: Optional[str] = None

class VQAResponse(BaseModel):
    response: str
    context: Optional[Dict[str, Any]] = None
    latency_ms: float
