import os
import jwt
from jwt import DecodeError


def jwt_encode(payload: dict[str, str]) -> str:
    secret_key = os.environ["SECRET_KEY"]
    token = jwt.encode(payload, secret_key)
    return token


def jwt_decode(token: str) -> None | dict[str, str]:
    secret_key = os.environ["SECRET_KEY"]
    try:
        return jwt.decode(
            token,
            secret_key,
            algorithms="HS256")
    except DecodeError:
        return None
