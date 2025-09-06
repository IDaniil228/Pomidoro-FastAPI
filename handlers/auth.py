from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import RedirectResponse

from Schema import UserCreateSchema, UserLoginSchema
from dependencies import get_auth_service
from exception import UserNotFoundException, WrongPasswordException
from service import AuthService

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/", response_model=UserLoginSchema)
async def login(
        username : str,
        password : str,
        auth_service : AuthService = Depends(get_auth_service),
):
    try:
        return await auth_service.login(username=username, password=password)
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

@router.get(
    "/login/google",
    response_class=RedirectResponse
)
async def google_login(
        auth_service : Annotated[AuthService, Depends(get_auth_service)]
):
    redirect_url = auth_service.get_google_redirect_url()
    print(redirect_url)
    return RedirectResponse(redirect_url)

@router.get(
    "/google",
)
async def google_auth(
        auth_service : Annotated[AuthService, Depends(get_auth_service)],
        code : str
):
    return await auth_service.google_auth(code=code)


@router.get(
    "/login/yandex",
    response_class=RedirectResponse
)
async def yandex_login(
        auth_service : Annotated[AuthService, Depends(get_auth_service)]
):
    redirect_url = auth_service.get_yandex_redirect_url()
    print(redirect_url)
    return RedirectResponse(redirect_url)

@router.get(
    "/yandex",
)
async def yandex_auth(
        auth_service : Annotated[AuthService, Depends(get_auth_service)],
        code : str
):
    return await auth_service.yandex_auth(code=code)