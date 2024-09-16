from sqlalchemy.orm import Session
from app.domain.models.user import User
from app.domain.repositories.user_repository import IUserRepository
from sqlalchemy.exc import NoResultFound

class SQLUserRepository(IUserRepository):
    def __init__(self, db_session: Session):
        self.db = db_session

    def create_user(self, user: User) -> User:
        db_user = User(**user.dict())
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def get_user_by_id(self, user_id: int) -> User:
        try:
            self.session.query(User).filter(User.id == user_id).first()
        except NoResultFound: 
            return None 