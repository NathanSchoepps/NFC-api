from pydantic import BaseModel

class UserBase(BaseModel):
    name: str
    nfc_data: str

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int

    class Config:
        orm_mode = True

class NFCData(BaseModel):
    uid: str
    data: str

class Token(BaseModel):
    access_token: str
    token_type: str
