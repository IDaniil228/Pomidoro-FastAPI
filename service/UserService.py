from dataclasses import dataclass

from Schema import UserSchema
from repository import UsersCacheRepository, UserRepository


@dataclass
class UserService:
    user_repository: UserRepository
    user_cache_repository: UsersCacheRepository

    def get_users(self):
        if users := self.user_cache_repository.get_all_users():
            return users
        else:
            users = self.user_repository.get_all_user()
            users_scheme_lst = [UserSchema.model_validate(user) for user in users]
            self.user_cache_repository.set_users(users_scheme_lst)
            return users