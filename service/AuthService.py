from dataclasses import dataclass
from datetime import datetime, timedelta
from os import access

from jose import jwt, JWTError

from Schema import UserLoginSchema, UserCreateSchema
from client import GoogleClient, YandexClient
from db.accessor import setting
from exception import UserNotFoundException, WrongPasswordException, TokenExpiredException, TokenNotCorrectException
from models import UserProfile
from repository import UserRepository

from setting import Setting

@dataclass
class AuthService:
    user_repository : UserRepository
    setting : Setting
    google_client : GoogleClient
    yandex_client : YandexClient

    def login(self, username : str, password: str) -> UserLoginSchema:
        user = self.user_repository.get_user_by_username(username)
        AuthService._validate_data(user, password)
        access_token = self.generate_access_token(user_id=user.id)
        return UserLoginSchema(user_id=user.id, access_token=access_token)

    def google_auth(self, code: str) -> UserLoginSchema:
        user_data = self.google_client.get_user_data(code=code)

        if user := self.user_repository.get_user_by_email(user_data.email):
            access_token = self.generate_access_token(user.id)
            return UserLoginSchema(user_id=user.id, access_token=access_token)

        user_create_schema = UserCreateSchema(**user_data.model_dump())
        created_user = self.user_repository.create_user(user_create_schema)
        print(user_data)
        access_token = self.generate_access_token(created_user.id)
        return UserLoginSchema(user_id=created_user.id, access_token=access_token)

    def yandex_auth(self, code: str) -> UserLoginSchema:
        user_data = self.yandex_client.get_user_data(code=code)
        print(user_data)

        if user := self.user_repository.get_user_by_email(user_data.email):
            access_token = self.generate_access_token(user.id)
            return UserLoginSchema(user_id=user.id, access_token=access_token)

        user_create_schema = UserCreateSchema(**user_data.model_dump())
        created_user = self.user_repository.create_user(user_create_schema)
        print(user_data)
        access_token = self.generate_access_token(created_user.id)
        return UserLoginSchema(user_id=created_user.id, access_token=access_token)


    def get_google_redirect_url(self) -> str:
        return self.setting.google_redirect_url


    def get_yandex_redirect_url(self) -> str:
        return self.setting.yandex_redirect_url





    @staticmethod
    def generate_access_token(user_id : int) -> str:
        data = {
            "user_id" : user_id,
            "exp" : datetime.now() + timedelta(days=1)
        }
        token : str = jwt.encode(data, setting.JWT_SECRET_KEY, setting.JWT_ALGORITHM)
        return token

    @staticmethod
    def get_used_id_from_access_token(access_token : str) -> int:
        try:
            data = jwt.decode(token=access_token, key=setting.JWT_SECRET_KEY, algorithms=[setting.JWT_ALGORITHM])
        except JWTError:
            raise TokenNotCorrectException
        if data["exp"] < datetime.now().timestamp():
            raise TokenExpiredException
        return data["user_id"]

    @staticmethod
    def _validate_data(user : UserProfile, password : str):
        if user is None:
            raise UserNotFoundException
        if user.password != password:
            raise WrongPasswordException


