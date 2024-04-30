
from dataclasses import dataclass
from exception import TokenExpireException, TokenNotCorrectException, UserNotCorrentPasswordException, UserNotFoundException
from models import User
from repository import UserRepository
from jose import jwt, JWTError
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
        access_token = self.generate_access_token(user_id=user.id)
        
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


    def get_user_id_from_access_token(self, access_token: str) -> int:
        try:
            payload = jwt.decode(access_token, self.settings.JWT_SECRET_KEY, algorithms=[self.settings.JWT_ALGORITHM])
        except JWTError:
            raise TokenNotCorrectException
        
        if payload['expire'] < dt.datetime.utcnow().timestamp():
            raise TokenExpireException

        return payload['user_id']