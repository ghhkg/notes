from typing import Protocol
from app.use_cases.common.interfaces import (
    UserCreator, UserChecker
)


class DbGateway(
    UserCreator, UserChecker,
    Protocol
):
    pass
