from fastapi import FastAPI
from app.presentation.api import api_router
from app.presentation.stubs import get_session_stub
from app.adapters.database.init_db import init_db


def create_app() -> FastAPI:
    myapp = FastAPI()
    myapp.include_router(api_router)
    return myapp


app = create_app()


@app.on_event("startup")
async def startup() -> None:
    session = await init_db()

    async def get_db():
        db = session()
        try:
            yield db
        finally:
            await db.close()

    app.dependency_overrides[get_session_stub] = get_db
