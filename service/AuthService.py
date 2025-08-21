from dataclasses import dataclass
from datetime import datetime, timedelta
from jose import jwt

from Schema import UserLoginSchema
from db.accessor import setting
from exception import UserNotFoundException, WrongPasswordException
from models import UserProfile
from repository import UserRepository
from setting import Setting


@dataclass
class AuthService():
    user_repository : UserRepository
    setting : Setting

    def login(self, username : str, password: str) -> UserLoginSchema:
        user = self.user_repository.get_user_by_username(username)
        AuthService._validate_data(user, password)
        access_token = self.generate_access_token(user_id=user.id)
        return UserLoginSchema(user_id=user.id, access_token=access_token)

    @staticmethod
    def generate_access_token(user_id : int) -> str:
        data = {
            "user_id" : user_id,
            "exp" : datetime.now() + timedelta(days=1)
        }
        token : str = jwt.encode(data, setting.JWT_SECRET_KEY, setting.JWT_ALGORITHM)
        return token

    @staticmethod
    def _validate_data(user : UserProfile, password : str):
        if user is None:
            raise UserNotFoundException
        if user.password != password:
            raise WrongPasswordException


