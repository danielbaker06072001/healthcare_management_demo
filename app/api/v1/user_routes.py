from fastapi import APIRouter, Depends
from app.core.user_service import UserService
from app.domain.models.user import User
from app.infrastructure.repositories.sql_user_repository import SQLUserRepository
from app.infrastructure.db.session import SessionLocal


router = APIRouter()


def get_user_service():
    db = SessionLocal()
    user_repo = SQLUserRepository(db)
    return UserService(user_repo)


@router.post("/users", response_model=User)
def create_user(user: User, user_service: UserService = Depends(get_user_service)):
    return user_service.create_user(user)


@router.get("/users/{user_id}", response_model=User)
def get_user(user_id: int, service: UserService = Depends(get_user_service)):
    return service.get_user_by_id(user_id)
