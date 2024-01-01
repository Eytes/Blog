from fastapi import FastAPI
import uvicorn

from post_manager.app.routers import (
    author,
)

app = FastAPI()
app.include_router(author.router)

if __name__ == '__main__':
    uvicorn.run("post_manager.app.main:app", reload=True)
