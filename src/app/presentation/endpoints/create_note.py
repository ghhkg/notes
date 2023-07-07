from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.presentation.stubs import get_session_stub
from app.presentation.schemas.note import Note
from app.adapters.database.crud import NoteCreatorImpl
from app.adapters.JWT import jwt_decode
from app.use_cases.create_note.use_case import CreateNoteService


router = APIRouter()


@router.post("/create_note")
async def create_note(
        note: Note,
        session: AsyncSession = Depends(get_session_stub)) -> dict[str, str]:
    jwt_payload = jwt_decode(
        note.jwt.token)
    if not jwt_payload:
        return {
            "status": "jwt incorrect"
        }
    user_id = jwt_payload["sub"]
    await CreateNoteService(
        NoteCreatorImpl(session)).create_note(
            user_id,
            note.text)
    return {
        "status": "ok"
    }
