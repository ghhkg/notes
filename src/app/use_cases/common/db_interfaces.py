from app.domain.models.user import User
from app.domain.models.note import Note
from typing import Protocol
from abc import abstractmethod


class UserCreator(Protocol):
    @abstractmethod
    async def register(
            self,
            user: User) -> None:
        raise NotImplementedError\


    @abstractmethod
    async def is_user_exist(
            self,
            username: str) -> bool:
        raise NotImplementedError


class UserAuthenticator(Protocol):
    @abstractmethod
    async def login(
            self,
            username: str) -> None | tuple[str, str]:
        raise NotImplementedError


class NoteCreator(Protocol):
    @abstractmethod
    async def create_note(
            self,
            note: Note) -> None:
        raise NotImplementedError


class NotesReader(Protocol):
    @abstractmethod
    async def read_notes(
            self,
            owner_id: str) -> list[Note]:
        raise NotImplementedError