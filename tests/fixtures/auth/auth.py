import pytest

from repository import UserRepository
from service import AuthService
from setting import Setting


@pytest.fixture
def mock_auth_service(google_client, yandex_client, fake_user_repository):
    return AuthService(
        user_repository=fake_user_repository,
        setting=Setting(),
        google_client=google_client,
        yandex_client=yandex_client
    )

@pytest.fixture
def auth_service(google_client, yandex_client, db_session):
    return AuthService(
        user_repository=UserRepository(db_session=db_session),
        setting=Setting(),
        google_client=google_client,
        yandex_client=yandex_client
    )