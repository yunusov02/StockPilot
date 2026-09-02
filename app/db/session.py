from collections.abc import AsyncIterator

from app.core.config import settings
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

engine = create_async_engine(
    settings.get_database_url(),
    echo=True,  # Set to True for debugging purposes, logs SQL statements
)

async_session = async_sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)


async def get_async_session() -> AsyncIterator[AsyncSession]: 
    """Get async database session"""
    async with async_session() as session:
        yield session
