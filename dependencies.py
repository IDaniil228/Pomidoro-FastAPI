from fastapi import Depends

from cache import get_redis_connection
from db import get_db_session

from repository import UserRepository, UsersCacheRepository
from service import UserService


def get_user_repository() -> UserRepository:
    return UserRepository(get_db_session())


def get_users_cache_repository() -> UsersCacheRepository:
    return UsersCacheRepository(get_redis_connection())




def get_users_service(
    user_repository: UserRepository = Depends(get_user_repository),
    user_cache_repository: UsersCacheRepository = Depends(get_users_cache_repository)
) -> UserService :
    return UserService(user_repository, user_cache_repository)