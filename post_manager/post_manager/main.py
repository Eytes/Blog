from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI

from post_manager.api_v1 import router as router_v1
from post_manager.core.config import settings
from post_manager.core.models import (
    Base,
    db_helper,
)


@asynccontextmanager
async def lifespan(app: FastAPI):
    # перед запуском приложения
    async with db_helper.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    yield
    # после запуска приложения


app = FastAPI(lifespan=lifespan)
app.include_router(router=router_v1, prefix=settings.api_v1_prefix)

if __name__ == "__main__":
    uvicorn.run("post_manager.main:app", reload=True)
