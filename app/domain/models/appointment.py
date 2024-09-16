from pydantic import BaseModel
from typing import Optional


class Appointment(BaseModel):
    id: Optional[int]
    user_id: int
    date: str
    time: str
    description: str
    status: str  # pending, confirmed, cancelled
