from typing import List
from app.domain.models.user import User


class IUserRepository:
    def create_user(self, user: User) -> User:
        raise NotImplementedError

    def get_user_by_id(self, user_id: int) -> User:
        raise NotImplementedError
