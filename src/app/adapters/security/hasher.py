from app.use_cases.common.hasher_interface import Hasher
from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError


class HasherImpl(Hasher):
    def __init__(self) -> None:
        self.ph = PasswordHasher()

    def hash_passwd(
            self,
            passwd: str) -> str:
        return self.ph.hash(passwd)

    def verify_passwd(
            self,
            hash_: str,
            passwd: str) -> bool:
        try:
            self.ph.verify(hash_, passwd)
            return True
        except VerifyMismatchError:
            return False
