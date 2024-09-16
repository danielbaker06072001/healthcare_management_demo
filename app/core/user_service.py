from app.domain.models.user import User
from app.domain.repositories.user_repository import IUserRepository


class UserService:
    def __init__(self, user_repository: IUserRepository):
        self.user_repository = user_repository

    def create_user(self, user: User) -> User:
        return self.user_repository.create_user(user)

    def get_user_by_id(self, user_id: int) -> User:
        return self.user_repository.get_user_by_id(user_id)
    
    def get_user_role(self, user_id: int) -> str:
        return self.user_repository.get_user_role(user_id)
