from pydantic import BaseModel
from typing import Optional


class User(BaseModel):
    role_id: Optional[int]
    role_name: str  # admin, provider, patient
    system_monitoring: bool
