from dataclasses import dataclass

import pytest

from Schema import GoogleUserDataSchema
from setting import Setting

from faker import Factory

@dataclass
class FakeGoogleClient:
    setting : Setting

    async def get_user_data(self, code : str) -> GoogleUserDataSchema:
        access_token = self._get_user_access_token(code=code)
        return google_user_data()

    def _get_user_access_token(self, code : str) -> str:
        return f"Fake access token {code}"

@dataclass
class FakeYandexClient:
    setting : Setting

    async def get_user_data(self, code : str) -> dict:
        access_token = self._get_user_access_token(code=code)
        return {"fake token" : access_token}

    def _get_user_access_token(self, code : str) -> str:
        return f"Fake access token {code}"


@pytest.fixture
def google_client():
    return FakeGoogleClient(setting=Setting())


@pytest.fixture
def yandex_client():
    return FakeYandexClient(setting=Setting())


faker = Factory.create()

def google_user_data() -> GoogleUserDataSchema:
    return GoogleUserDataSchema(
        id=faker.random_int(),
        email=faker.email(),
        name=faker.name(),
        google_access_token=faker.sha256()
    )