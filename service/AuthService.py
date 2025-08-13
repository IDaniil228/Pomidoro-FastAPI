from dataclasses import dataclass
from os import access

from Schema import UserLoginSchema
from exception import UserNotFoundException, WrongPasswordException
from models import UserProfile
from repository import UserRepository


@dataclass
class AuthService():
    user_repository : UserRepository

    def login(self, username : str, password: str) -> UserLoginSchema:
        user = self.user_repository.get_user_by_username(username)
        AuthService._validate_data(user, password)
        return UserLoginSchema(user_id=user.id, access_token=user.access_token)

    @staticmethod
    def _validate_data(user : UserProfile, password : str):
        if user is None:
            raise UserNotFoundException
        if user.password != password:
            raise WrongPasswordException
