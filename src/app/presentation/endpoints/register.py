from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.presentation.stubs import get_session_stub
from app.presentation.schemas.user import User
from app.adapters.database.crud import UserCreatorImpl
from app.adapters.JWT import jwt_encode
from app.adapters.security.hasher import HasherImpl
from app.use_cases.common.exceptions import UserExistError
from app.use_cases.registration.use_case import RegistrationService


router = APIRouter()


@router.post("/register")
async def register(
        user: User,
        session: AsyncSession = Depends(get_session_stub)) -> dict[str, str]:
    try:
        user_id = await RegistrationService(
            UserCreatorImpl(session),
            HasherImpl()).register(
                user.login,
                user.passwd
        )
    except UserExistError:
        return {
            "status": "user exist",
            "jwt": ""
        }
    token = jwt_encode({"sub": user_id})
    return {
        "status": "ok",
        "jwt": token
    }
