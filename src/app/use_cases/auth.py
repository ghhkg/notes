from app.use_cases.common.hasher_interface import Hasher
from app.use_cases.common.db_interfaces import UserAuthenticator
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
        user_info = await self.db_service.login(username)
        if not user_info:
            raise UserDataIncorrect
        right_passwd, user_id = user_info
        is_passwd_right = self.hasher_service.verify_passwd(
            right_passwd,
            passwd)
        if is_passwd_right:
            return user_id
        raise UserDataIncorrect
