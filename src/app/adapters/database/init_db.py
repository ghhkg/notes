import os
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.asyncio import async_sessionmaker
from app.adapters.database.base import Base


async def init_db() -> async_sessionmaker[AsyncSession]:
    engine = create_async_engine(os.environ["dsn"])
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    return async_sessionmaker(bind=engine)
