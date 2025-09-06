import httpx
from fastapi import Depends, Request, security, Security, HTTPException

from cache import get_redis_connection
from client import GoogleClient, YandexClient
from db import get_db_session

from sqlalchemy.ext.asyncio import AsyncSession

from exception import TokenExpiredException, TokenNotCorrectException
from repository import UserRepository, UsersCacheRepository, TaskRepository
from service import UserService, AuthService

import redis

from service.TaskService import TaskService
from setting import Setting


async def get_async_client():
    return httpx.AsyncClient()

async def get_google_client(async_client : httpx.AsyncClient = Depends(get_async_client)) -> GoogleClient:
    setting = Setting()
    return GoogleClient(setting=setting, async_client=async_client)

async def get_yandex_client(async_client : httpx.AsyncClient = Depends(get_async_client)) -> YandexClient:
    setting = Setting()
    return YandexClient(setting=setting, async_client=async_client)

async def get_task_repository(
        session : AsyncSession = Depends(get_db_session)
) -> TaskRepository:
    return TaskRepository(db_session=session)

async def get_task_service(
        task_repository : TaskRepository = Depends(get_task_repository)
) -> TaskService:
    return TaskService(task_repository=task_repository)


async def get_user_repository(db_session: AsyncSession = Depends(get_db_session)) -> UserRepository:
    return UserRepository(db_session=db_session)


async def get_users_cache_repository(redis: redis.Redis = Depends(get_redis_connection)) -> UsersCacheRepository:
    return UsersCacheRepository(redis=redis)

async def get_auth_service(
        user_repository : UserRepository = Depends(get_user_repository),
        google_client : GoogleClient = Depends(get_google_client),
        yandex_client : YandexClient = Depends(get_yandex_client)
) -> AuthService:
    setting : Setting = Setting()
    return AuthService(user_repository=user_repository,
                       setting=setting,
                       google_client=google_client,
                       yandex_client=yandex_client)

async def get_users_service(
    user_repository: UserRepository = Depends(get_user_repository),
    user_cache_repository: UsersCacheRepository = Depends(get_users_cache_repository),
    auth_service: AuthService = Depends(get_auth_service)
) -> UserService :
    return UserService(
        user_repository=user_repository,
        user_cache_repository=user_cache_repository,
        auth_service=auth_service
    )

reusable_auth2 = security.HTTPBearer()

async def get_request_user_id(
        request : Request,
        token : security.http.HTTPAuthorizationCredentials = Security(reusable_auth2),
        auth_service : AuthService = Depends(get_auth_service)
) -> int:
    try:
        return auth_service.get_used_id_from_access_token(token.credentials)
    except TokenExpiredException as e:
        raise HTTPException(
            status_code=401,
            detail=e.detail
        )
    except TokenNotCorrectException as e:
        raise HTTPException(
            status_code=401,
            detail=e.detail
        )