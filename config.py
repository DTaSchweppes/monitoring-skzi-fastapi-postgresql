from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

engine = create_async_engine("postgresql://username:password@localhost/dbname", future=True)

# Создаем фабрику сессий
SessionFactory = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

# Функция для создания асинхронной сессии базы данных
async def get_db_session() -> AsyncSession:
    async with SessionFactory() as session:
        yield session
