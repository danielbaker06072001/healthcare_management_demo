from sqlalchemy.orm import Session
from app.domain.models.user_claims import UserClaims
from app.domain.repositories.token_repository import ITokenRepository
from sqlalchemy.exc import NoResultFound

class SQLTokenRepository(ITokenRepository):
    def __init__(self, db_session: Session):
        self.db = db_session

    def save_token(): 
        return NotImplemented