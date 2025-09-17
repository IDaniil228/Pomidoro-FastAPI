import pytest

import asyncio

pytest_plugins = [
    "tests.fixtures.auth.auth",
    "tests.fixtures.auth.clients",
    "tests.fixtures.user.user_repository",
    "tests.fixtures.user.user_model",
    "tests.fixtures.infrastructure"
]

@pytest.fixture(scope="session")
def event_loop():
    loop = asyncio.get_event_loop()
    yield
    loop.close()