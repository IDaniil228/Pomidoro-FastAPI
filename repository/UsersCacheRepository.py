import json

from redis import asyncio as Redis

from Schema import UserCreateSchema, UserLoginSchema

class UsersCacheRepository:
    def __init__(self, redis: Redis):
        self.redis = redis

    async def get_all_users(self) -> list[UserCreateSchema]:
        async with self.redis as redis:
            users_json = await redis.lrange("users", 0, -1)
            users_lst = [UserCreateSchema.model_validate(json.loads(user)) for user in users_json]
            return users_lst

    async def set_users(self, users: list[UserLoginSchema]):
        if len(users) == 0:
            return
        users_json = [user.model_dump_json()  for user in users]
        async with self.redis as redis:
            await redis.lpush("users", *users_json)