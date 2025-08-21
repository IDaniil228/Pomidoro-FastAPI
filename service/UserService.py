from dataclasses import dataclass

from Schema import UserLoginSchema, UserLoginSchema
from repository import UsersCacheRepository, UserRepository
from service.AuthService import AuthService


@dataclass
class UserService:
    auth_service : AuthService
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
        user = self.user_repository.create_user(username=username, password=password)
        access_token = AuthService.generate_access_token(user_id=user.id)
        return UserLoginSchema(user_id=user.id, access_token=access_token)