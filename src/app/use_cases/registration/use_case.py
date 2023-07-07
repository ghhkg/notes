from app.domain.models.user import User
from app.use_cases.common.exceptions import UserExistError
from app.use_cases.common.interfaces import Hasher
from uuid import uuid4
from .interfaces import DbGateway


class RegistrationService:
    def __init__(
            self,
            db_service: DbGateway,
            hasher_service: Hasher) -> None:
        self.db_service = db_service
        self.hasher_service = hasher_service

    async def register(
            self,
            username: str,
            passwd: str) -> str:
        if not await self.db_service.is_user_exist(username):
            user_id = uuid4().hex
            await self.db_service.register(
                User(
                    user_id=user_id,
                    username=username,
                    passwd=self.hasher_service.hash_passwd(passwd))
            )
            return user_id
        raise UserExistError()
