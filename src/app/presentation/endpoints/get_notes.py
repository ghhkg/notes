from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.presentation.stubs import get_session_stub
from app.presentation.schemas.note import JWT
from app.adapters.database.crud import NotesReaderImpl
from app.adapters.JWT import jwt_decode
from app.use_cases.read_user_notes.use_case import ReadNotesService


router = APIRouter()


@router.post("/get_notes")
async def get_notes(
        token: JWT,
        session: AsyncSession = Depends(get_session_stub)) -> dict[str, str | list[str]]:
    jwt_payload = jwt_decode(token.token)
    if not jwt_payload:
        return {
            "status": "jwt incorrect"
        }
    user_id = jwt_payload["sub"]
    notes = await ReadNotesService(
        NotesReaderImpl(session)).read_notes(user_id)
    return {
        "status": "ok",
        "notes": notes
    }
