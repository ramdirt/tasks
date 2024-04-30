
from dataclasses import dataclass
from exception import UserNotCorrentPasswordException, UserNotFoundException
from models import User
from repository import UserRepository
from jose import jwt
import datetime as dt
from datetime import timedelta 

from schema import UserLoginSchema
from settings import Settings


@dataclass
class AuthService:
    user_repository: UserRepository
    settings: Settings
    

    def login(self, username: str, password: str) -> UserLoginSchema:

        user = self.user_repository.get_user_by_username(username)

        self._validate_auth_user(user, password)
        access_token = self._generate_access_token(user_id=user.id)
        
        return UserLoginSchema(user_id=user.id, access_token=access_token)
    
    @staticmethod
    def _validate_auth_user(user: User, password: str):
        if not user:
            raise UserNotFoundException
        if user.password != password:
            raise UserNotCorrentPasswordException
        

    def generate_access_token(self, user_id: int) -> str:
        expire_date_unix = (dt.datetime.utcnow() + timedelta(days=7)).timestamp()
        token = jwt.encode(
            {
                'user_id': user_id,
                'expire': expire_date_unix
            },
            self.settings.JWT_SECRET_KEY,
            algorithm=self.settings.JWT_ALGORITHM
        )
        
        return token
