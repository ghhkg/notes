from sqlalchemy.orm import Mapped, mapped_column
from app.adapters.database.base import Base


class Users(Base):
    __tablename__ = "Users"
    user_id: Mapped[str] = mapped_column(primary_key=True)
    login: Mapped[str]
    passwd: Mapped[str]


class Notes(Base):
    __tablename__ = "Notes"
    note_id: Mapped[str] = mapped_column(primary_key=True)
    owner_id: Mapped[str]
    text: Mapped[str]
