from fastapi import Depends, Request, security, Security, HTTPException

from cache import get_redis_connection
from client import GoogleClient
from db import get_db_session

from sqlalchemy.orm import Session

from exception import TokenExpiredException, TokenNotCorrectException
from repository import UserRepository, UsersCacheRepository, TaskRepository
from service import UserService, AuthService

import redis

from service.TaskService import TaskService
from setting import Setting



def get_google_client():
    setting = Setting()
    return GoogleClient(setting=setting)

def get_task_repository(
        session : Session = Depends(get_db_session)
) -> TaskRepository:
    return TaskRepository(db_session=session)

def get_task_service(
        task_repository : TaskRepository = Depends(get_task_repository)
) -> TaskService:
    return TaskService(task_repository=task_repository)


def get_user_repository(db_session: Session = Depends(get_db_session)) -> UserRepository:
    return UserRepository(db_session=db_session)


def get_users_cache_repository(redis: redis.Redis = Depends(get_redis_connection)) -> UsersCacheRepository:
    return UsersCacheRepository(redis=redis)

def get_auth_service(
        user_repository : UserRepository = Depends(get_user_repository),
        google_client : GoogleClient = Depends(get_google_client)
) -> AuthService:
    setting : Setting = Setting()
    return AuthService(user_repository=user_repository,
                       setting=setting,
                       google_client=google_client)

def get_users_service(
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

def get_request_user_id(
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