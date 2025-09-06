from dataclasses import dataclass

from Schema import UserLoginSchema, UserLoginSchema, UserCreateSchema
from repository import UsersCacheRepository, UserRepository
from service.AuthService import AuthService


@dataclass
class UserService:
    auth_service : AuthService
    user_repository: UserRepository
    user_cache_repository: UsersCacheRepository

    async def get_users(self) -> list[UserCreateSchema]:
        if users := await self.user_cache_repository.get_all_users():
            return users
        else:
            users = await self.user_repository.get_all_user()
            users_scheme_lst = [UserCreateSchema.model_validate(user) for user in users]
            return users_scheme_lst

    async def create_user(self, username: str, password: str) -> UserLoginSchema:
        user = await self.user_repository.create_user(username=username, password=password)
        access_token = AuthService.generate_access_token(user_id=user.id)
        return UserLoginSchema(user_id=user.id, access_token=access_token)