from asyncio import current_task

from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
    async_scoped_session,
    AsyncSession,
)

from post_manager.core.config import settings


class DatabaseHelper:
    def __init__(self, url: str, echo: bool = False):
        self.engine = create_async_engine(
            url=url,
            echo=echo,
        )
        self.session_factory = async_sessionmaker(
            bind=self.engine,
            autoflush=False,
            autocommit=False,
            expire_on_commit=False,
        )

    def get_scoped_session(self):
        """Создание частной сессии"""
        session = async_scoped_session(
            session_factory=self.session_factory,
            scopefunc=current_task,  # правило получения текущего пространства
        )
        return session

    async def session_dependency(self) -> AsyncSession:
        """Создание сессии для каждого запроса и ее закрытие"""
        async with self.session_factory() as session:
            yield session
            await session.close()

    async def scoped_session_dependency(self) -> AsyncSession:
        """Создание сессии для одной области и ее закрытие. Можно переиспользовать сессию"""
        session = self.get_scoped_session()
        yield session
        await session.close()


db_helper = DatabaseHelper(
    url=settings.db.url,
    echo=settings.db.echo,
)
