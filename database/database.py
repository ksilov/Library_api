from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from .config import settings
from .models import Base


engine = create_async_engine(settings.get_url, echo=True, future=True)
AsyncSessionLocal = async_sessionmaker(bind=engine)


async def create_tables():
    async with engine.begin() as connect:
        await connect.run_sync(Base.metadata.create_all)
        await connect.commit()


async def delete_tables():
    async with engine.begin() as connect:
        await connect.run_sync(Base.metadata.drop_all)
        await connect.commit()


async def get_session():
    async with AsyncSessionLocal() as session:
        yield session





