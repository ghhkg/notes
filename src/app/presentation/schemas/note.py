from pydantic import BaseModel


class JWT(BaseModel):
    token: str


class Note(BaseModel):
    jwt: JWT
    text: str
