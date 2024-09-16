from pydantic import BaseModel
from typing import Optional, List


class UserClaims(BaseModel) : 
    userId: Optional[int]
    iss: str # Issuer (name of healthcare system)
    sub: str 
    aud: str # Audience 
    exp: int # Expired time  
    nbf: int 
    iat: int # Issued at 
    jti: str # Jwt_id
    roles: List[str] # Roles 
    
class TokenRequest(BaseModel): 
    UserId: str

class AccessToken(BaseModel): 
    # * This will be a JWT of UserClaims (signs with SECRETKEY)
    # ? TODO: Use public / private key for extra security
    AccessToken: str 
    
    Type: str       # mostly bearer