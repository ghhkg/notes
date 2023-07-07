from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.presentation.stubs import get_session_stub
from app.presentation.schemas.user import User
from app.adapters.database.crud import UserAuthenticatorImpl
from app.adapters.JWT import jwt_encode
from app.adapters.security.hasher import HasherImpl
from app.use_cases.common.exceptions import UserDataIncorrect
from app.use_cases.auth.use_case import AuthorizationService


router = APIRouter()


@router.post("/login")
async def login(
        user: User,
        session: AsyncSession = Depends(get_session_stub)) -> dict[str, str]:
    try:
        user_id = await AuthorizationService(
            UserAuthenticatorImpl(session),
            HasherImpl()).login(
                user.login,
                user.passwd
        )
    except UserDataIncorrect:
        return {
            "status": "data incorrect",
            "jwt": ""
        }
    token = jwt_encode({"sub": user_id})
    return {
        "status": "ok",
        "jwt": token
    }
