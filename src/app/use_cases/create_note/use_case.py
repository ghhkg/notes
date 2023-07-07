from app.domain.models.note import Note
from app.use_cases.common.interfaces import NoteCreator
from uuid import uuid4


class CreateNoteService:
    def __init__(
            self,
            db_service: NoteCreator):
        self.db_service = db_service

    async def create_note(
            self,
            user_id: str,
            text: str) -> None:
        await self.db_service.create_note(
            Note(
                note_id=uuid4().hex,
                owner_id=user_id,
                text=text)
        )
