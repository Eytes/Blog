from fastapi import APIRouter

from post_manager.api_v1.authors.views import router as authors_router
from post_manager.api_v1.comments.views import router as comments_router
from post_manager.api_v1.likes.views import router as likes_router
from post_manager.api_v1.posts.views import router as posts_router
from post_manager.api_v1.topics.views import router as topics_router

router = APIRouter()
router.include_router(router=authors_router, prefix="/authors")
router.include_router(router=posts_router, prefix="/posts")
router.include_router(router=topics_router, prefix="/topics")
router.include_router(router=comments_router, prefix="/comments")
router.include_router(router=likes_router, prefix="/likes")
