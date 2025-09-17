from datetime import  timezone, datetime, timedelta

import pytest

from Schema import UserLoginSchema
from models import UserProfile
from service import AuthService
from setting import Setting

from jose import jwt

pytestmark = pytest.mark.asyncio

def test_get_google_redirect_url__success(mock_auth_service: AuthService, setting: Setting):
    setting_google_redirect_url = setting.google_redirect_url
    auth_service_google_redirect_url = mock_auth_service.get_google_redirect_url()
    assert setting_google_redirect_url == auth_service_google_redirect_url


def test_get_yandex_redirect_url__success(mock_auth_service: AuthService, setting: Setting):
    setting_yandex_redirect_url = setting.yandex_redirect_url
    auth_service_yandex_redirect_url = mock_auth_service.get_yandex_redirect_url()
    assert setting_yandex_redirect_url == auth_service_yandex_redirect_url


def test_generate_jwt__success(mock_auth_service: AuthService, setting: Setting):
    user_id = 1
    access_token = mock_auth_service.generate_access_token(user_id=user_id)
    user_id_from_access_token = mock_auth_service.get_user_id_from_access_token(access_token)
    expire_access_token = datetime.fromtimestamp(
        jwt.decode(
            token=access_token,
            key=setting.JWT_SECRET_KEY,
            algorithms=setting.JWT_ALGORITHM)["exp"],
            tz=timezone.utc
    )
    assert user_id == user_id_from_access_token
    assert (expire_access_token - datetime.now(tz=timezone.utc)) < timedelta(days=1)


async def test_google_auth__success(mock_auth_service: AuthService):
    code = "fake code"

    user = await mock_auth_service.google_auth(code=code)
    user_id = user.user_id
    access_token = user.access_token
    gecode_id = mock_auth_service.get_user_id_from_access_token(access_token=access_token)

    assert user_id == gecode_id
    assert isinstance(user, UserLoginSchema)