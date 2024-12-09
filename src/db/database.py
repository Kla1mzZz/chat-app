from typing import Any, AsyncGenerator
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase
from settings import settings


engine = create_async_engine(settings.database_url)

async_session = async_sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)

async def get_session() -> AsyncGenerator[AsyncSession, Any]:
    async with async_session() as session:
        yield session

class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(primary_key=True)