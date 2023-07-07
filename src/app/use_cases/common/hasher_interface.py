from typing import Protocol
from abc import abstractmethod


class Hasher(Protocol):
    @abstractmethod
    def hash_passwd(
            self,
            passwd: str) -> str:
        raise NotImplementedError

    @abstractmethod
    def verify_passwd(
            self,
            hash_: str,
            passwd: str) -> bool:
        raise NotImplementedError
