from dataclasses import dataclass
from typing import NewType


@dataclass
class User:
    user_id: str
    username: str
    passwd: str
