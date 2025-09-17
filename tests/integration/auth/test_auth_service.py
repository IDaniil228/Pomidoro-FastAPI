from service import AuthService

import pytest

pytestmark = pytest.mark.asyncio

async def test_google_auth__success(auth_service : AuthService, db_session):
    code = "fake code"

    user = await auth_service.google_auth(code=code)

    assert user is not None
