from app.use_cases.common.interfaces import NotesReader


class ReadNotesService:
    def __init__(
            self,
            db_service: NotesReader):
        self.db_service = db_service

    async def read_notes(
            self,
            user_id: str) -> list[str]:
        notes = await self.db_service.read_notes(user_id)
        return [note.text for note in notes]
