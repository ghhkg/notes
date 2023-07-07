from fastapi import APIRouter

from app.presentation.endpoints import (
    register, login,
    create_note, get_notes,
)

api_router = APIRouter(prefix="/api")
api_router.include_router(register.router)
api_router.include_router(login.router)
api_router.include_router(create_note.router)
api_router.include_router(get_notes.router)
