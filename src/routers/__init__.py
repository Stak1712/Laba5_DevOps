from fastapi import APIRouter

from .user import router as user

router = APIRouter(prefix="/api/v1")
router.include_router(user, prefix="/user", tags=["User"])
