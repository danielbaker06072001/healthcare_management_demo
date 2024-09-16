from datetime import datetime, timedelta
from jose import jwt, JWTError
from passlib.context import CryptContext
from app.domain.repositories.token_repository import ITokenRepository

SECRET_KEY = "demo_key_later_will_use_generated_key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60    # 1 hour
EXPECTED_AUDIENCE = "healthcare_users"

# Hashing services 
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def create_access_token(data: dict) : 
    to_encode = data.copy() 
    expire = datetime.now(datetime.timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)


# Implementing Token Services that depends on UserRepository interface
class TokenService:
    def __init__(self, token_repository: ITokenRepository): 
        self.token_repository = token_repository

    def authenticate_user(self, username: str, password : str) -> bool : 
        # TODO : implement user retrieval here (retrieved from db) 
        # *user = self.user_repository.get_user_by_username(username) 
        user = None
        if not user : 
            return False
        if not self.verify_password(password, user.pasword) :
            return False
        return user 

    '''
        * Function that create access token that used the predefined secret key 
        TODO:
            - We can increase the security of this by using generated public / private key on our machine
            - We could increase more of the security by switching, each token will have a different pair of public and private key
    '''
    def create_access_token(self, data: dict, expires_delta: timedelta = None) -> str: 
        to_encode = data.copy().dict()
        if expires_delta: 
            expire = datetime.utcnow().timestamp() + expires_delta
        else : # *if token is expired then generate new expire 
            expire = datetime.utcnow().timestamp() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(claims=to_encode, key=SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt
    
    def verify_access_token(self, token: dict) : 
        decoded_jwt = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM],
            audience=EXPECTED_AUDIENCE,  # Add this to check the audience claim
            options={"verify_nbf": False}  # You can modify the options based on your needs
        )
        return decoded_jwt
    
    def hash_password(self, password: str) : 
        return pwd_context.hash(password)

    def verify_password(self, plain_password : str, hashed_password: str)  :
        return pwd_context.verify(plain_password, hashed_password)
    

    
    