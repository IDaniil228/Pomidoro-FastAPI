import string

from dataclasses import dataclass
from random import choice

from Schema import UserLoginSchema, UserLoginSchema
from repository import UsersCacheRepository, UserRepository


@dataclass
class UserService:
    user_repository: UserRepository
    user_cache_repository: UsersCacheRepository

    def get_users(self) -> list[UserLoginSchema]:
        if users := self.user_cache_repository.get_all_users():
            return users
        else:
            users = self.user_repository.get_all_user()
            users_scheme_lst = [UserLoginSchema.model_validate(user) for user in users]
            self.user_cache_repository.set_users(users_scheme_lst)
            return users

    def create_user(self, username: str, password: str) -> UserLoginSchema:
        access_token = self._generate_access_token()
        user = self.user_repository.create_user(username, password, access_token)
        return UserLoginSchema(user_id=user.id, access_token=access_token)

    @staticmethod
    def _generate_access_token() -> str:
        return "".join(choice(string.ascii_uppercase + string.digits) for _ in range(10))