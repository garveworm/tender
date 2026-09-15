from collections.abc import AsyncIterator, Iterator

import pytest
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, create_async_engine
from testcontainers.community.postgres import PostgresContainer


@pytest.fixture(scope="module")
def postgres_container() -> Iterator[PostgresContainer]:
    with PostgresContainer("postgres:16", driver="asyncpg") as container:
        yield container


@pytest.fixture
async def engine(postgres_container: PostgresContainer) -> AsyncIterator[AsyncEngine]:
    engine = create_async_engine(postgres_container.get_connection_url())
    yield engine
    await engine.dispose()


async def test_can_connect_and_query(engine: AsyncEngine) -> None:
    async with AsyncSession(engine, expire_on_commit=False) as session:
        result = await session.execute(text("SELECT 1"))
        assert result.scalar_one() == 1
