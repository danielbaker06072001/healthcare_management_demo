from pydantic import BaseModel
from typing import Optional


class User(BaseModel):
    user_id: Optional[int]
    name: str
    email: str
    password: str
    role: str  # admin, guest, patient
    role_id: Optional[int] 
