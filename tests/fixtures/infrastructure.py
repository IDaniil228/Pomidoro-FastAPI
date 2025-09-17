import pytest
import pytest_asyncio

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

from db.database import Base

from setting import Setting

@pytest.fixture
def setting():
    return Setting()


engine = create_async_engine(url="postgresql+asyncpg://hh:1234@localhost:5432/test", future=True, echo=True, pool_pre_ping=True)

AsyncSessionFactory = async_sessionmaker(engine, autoflush=False, expire_on_commit=False)


@pytest_asyncio.fixture(scope="session", autouse=True)
async def init_model(event_loop):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)


@pytest_asyncio.fixture
async def db_session() -> AsyncSession:
    return AsyncSessionFactory()