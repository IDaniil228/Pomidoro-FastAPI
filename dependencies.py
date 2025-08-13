from fastapi import Depends

from cache import get_redis_connection
from db import get_db_session

from sqlalchemy.orm import Session

from repository import UserRepository, UsersCacheRepository
from service import UserService, AuthService

import redis


def get_user_repository(db_session: Session = Depends(get_db_session)) -> UserRepository:
    return UserRepository(db_session=db_session)


def get_users_cache_repository(redis: redis.Redis = Depends(get_redis_connection)) -> UsersCacheRepository:
    return UsersCacheRepository(redis=redis)


def get_users_service(
    user_repository: UserRepository = Depends(get_user_repository),
    user_cache_repository: UsersCacheRepository = Depends(get_users_cache_repository)
) -> UserService :
    return UserService(user_repository, user_cache_repository)


def get_auth_service(
        user_repository : UserRepository = Depends(get_user_repository)
):
    return AuthService(user_repository)