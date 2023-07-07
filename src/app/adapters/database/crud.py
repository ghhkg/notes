from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.domain.models.user import User
from app.domain.models.note import Note
from app.adapters.database.models import Users, Notes
from app.use_cases.common.db_interfaces import (
    UserCreator,
    UserAuthenticator,
    NoteCreator,
    NotesReader
)


class UserCreatorImpl(UserCreator):
    def __init__(
            self,
            session: AsyncSession) -> None:
        self.session = session

    async def is_user_exist(
            self,
            username: str) -> bool:
        stmt = select(Users).where(Users.login == username)
        for _ in await self.session.execute(stmt):
            await self.session.close()
            return True
        return False

    async def register(
            self,
            user: User) -> None:
        self.session.add(
            Users(
                user_id=user.user_id,
                login=user.username,
                passwd=user.passwd)
        )
        await self.session.commit()


class UserAuthenticatorImpl(UserAuthenticator):
    def __init__(
            self,
            session: AsyncSession) -> None:
        self.session = session

    async def login(
            self,
            username: str) -> None | tuple[str, str]:
        stmt = select(Users).where(
            Users.login == username)
        for row in await self.session.execute(stmt):
            user_info = row[0]
            right_passwd = user_info.passwd
            user_id = user_info.user_id
            return right_passwd, user_id


class NoteCreatorImpl(NoteCreator):
    def __init__(
            self,
            session: AsyncSession) -> None:
        self.session = session

    async def create_note(
            self,
            note: Note) -> None:
        self.session.add(
            Notes(
                note_id=note.note_id,
                owner_id=note.owner_id,
                text=note.text)
        )
        await self.session.commit()


class NotesReaderImpl(NotesReader):
    def __init__(
            self,
            session: AsyncSession) -> None:
        self.session = session

    async def read_notes(
            self,
            owner_id: str) -> list[Note]:
        notes = []
        stmt = select(Notes).where(
            Notes.owner_id == owner_id)
        for row in await self.session.execute(stmt):
            note = row[0]
            notes.append(
                Note(
                    note_id=note.note_id,
                    owner_id=note.owner_id,
                    text=note.text)
            )
        return notes
