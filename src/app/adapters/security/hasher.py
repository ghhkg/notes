from app.use_cases.common.interfaces import Hasher


class HasherImpl(Hasher):
    def hash_passwd(
            self,
            passwd: str) -> str:
        return passwd
