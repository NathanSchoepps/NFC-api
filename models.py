from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    email: str
    role: str

class Token(BaseModel):
    access_token: str
    token_type: str

class NFCData(BaseModel):
    token: str
