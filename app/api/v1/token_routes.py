from datetime import datetime
from fastapi import APIRouter, Depends
from app.core.token_service import TokenService
from app.domain.models.user_claims import UserClaims, TokenRequest, AccessToken
from app.infrastructure.repositories.sql_token_repository import SQLTokenRepository
from app.infrastructure.db.session import SessionLocal
from passlib.context import CryptContext
from typing import Dict, Any

router = APIRouter()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_token_service():
    # token_repo = SQLUserRepository(db)      # TODO: changed to token repo (implemented the UserRepo)
    # return TokenService(token_repo)
    db = None
    token_repo =  SQLTokenRepository(db)
    return TokenService(token_repo)

# ! This is just a demo, but further more in the project, this route will call domain, usecase, infras layer through Interface
# ? This api and the one below shows that the different between using Model and dict (any) as input model
@router.post("/create_claims", response_model=UserClaims)
def create_claims(payload: TokenRequest, token_service : TokenService = Depends(get_token_service)): 
    print(payload)
    
    # ! Test claims
    return UserClaims(
        userId=123,  # Example valid integer for UserId
        iss="healthcare_system",  # Issuer (your system name)
        sub="subject_of_token",   # Subject of the token
        aud="healthcare_users",   # Audience (intended audience of the token)
        exp=int(datetime.utcnow().timestamp()) + 3600,  # Expiration time in seconds from now
        nbf=int(datetime.utcnow().timestamp()),  # Not before (current time)
        iat=int(datetime.utcnow().timestamp()),  # Issued at (current time)
        jti="unique_jwt_id_123",  # Unique JWT ID
        roles=["admin", "user"]  # Example roles
    )

# ! This is the demo for creating access_token, obviously this is not too well secure, will be developed when received proposal from client
@router.post("/create_access_token", response_model=AccessToken)
def create_access_token(payload: dict, token_service: TokenService = Depends(get_token_service)):  
    test_claims = create_claims(payload=payload)
    access_token = token_service.create_access_token(test_claims, 60)
    
    return AccessToken(
        AccessToken = access_token, 
        Type = "Bearer"
    )

# ? Demo token parser, very basic one
@router.post("/verify_token", response_model=Any)
def verify_token(payload: Dict[str, str],  token_service: TokenService = Depends(get_token_service)):
    response = token_service.verify_access_token(token=payload.get("access_token"))
    return response