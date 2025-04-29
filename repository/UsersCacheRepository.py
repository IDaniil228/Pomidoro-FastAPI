import json

from redis import Redis

from Schema.UserSchema import UserSchema


class UsersCacheRepository:
    def __init__(self, redis: Redis):
        self.redis = redis

    def get_all_users(self) -> list[UserSchema]:
        with self.redis as redis:
            users_json = redis.lrange("users", 0, -1)
            users_lst = [UserSchema.model_validate(json.loads(user)) for user in users_json]
            return users_lst

    def set_users(self, users: list[UserSchema]):
        users_json = [user.model_dump_json()  for user in users]
        with self.redis as redis:
            redis.lpush("users", *users_json)


