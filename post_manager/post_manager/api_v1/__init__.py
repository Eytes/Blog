from fastapi import APIRouter

from post_manager.api_v1.authors.views import router as authors_router

router = APIRouter()
router.include_router(router=authors_router, prefix="/authors")
