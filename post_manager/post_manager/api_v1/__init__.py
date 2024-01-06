from fastapi import APIRouter

from post_manager.api_v1.authors.views import router as authors_router
from post_manager.api_v1.posts.views import router as posts_router

router = APIRouter()
router.include_router(router=authors_router, prefix="/authors")
router.include_router(router=posts_router, prefix="/posts")
