from fastapi import FastAPI

from post_manager.app.routers import (
    author,
)

app = FastAPI()
app.include_router(author.router)
