from fastapi import APIRouter, Depends, HTTPException

from Schema import UserCreateSchema, UserLoginSchema
from dependencies import get_auth_service
from exception import UserNotFoundException, WrongPasswordException
from service import AuthService

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/", response_model=UserLoginSchema)
def login(
        body : UserCreateSchema,
        auth_service : AuthService = Depends(get_auth_service)
):
    try:
        return auth_service.login(body.username, body.password)
    except UserNotFoundException as e:
        raise HTTPException(
            status_code=404,
            detail=e.detail
        )
    except WrongPasswordException as e:
        raise HTTPException(
            status_code=401,
            detail=e.detail
        )