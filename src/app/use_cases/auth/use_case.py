from app.use_cases.common.interfaces import (
    UserAuthenticator, Hasher
)
from app.use_cases.common.exceptions import UserDataIncorrect


class AuthorizationService:
    def __init__(
            self,
            db_service: UserAuthenticator,
            hasher_service: Hasher):
        self.db_service = db_service
        self.hasher_service = hasher_service

    async def login(
            self,
            username: str,
            passwd: str) -> str:
        user_id = await self.db_service.login(
            username,
            self.hasher_service.hash_passwd(passwd))
        if user_id:
            return user_id
        raise UserDataIncorrect
