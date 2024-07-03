from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.crud import get_user_by_nfc_data, create_user
from app.schemas import NFCData, Token, UserCreate, User
from app.database import get_db
from app.auth import authenticate_with_external_service

router = APIRouter()

@router.post("/nfc-auth/", response_model=Token)
async def nfc_auth(nfc_data: NFCData, db: AsyncSession = Depends(get_db)):
    user = await get_user_by_nfc_data(db, nfc_data.data)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    token = authenticate_with_external_service(nfc_data)
    return token

@router.post("/users/", response_model=User)
async def create_user_endpoint(user: UserCreate, db: AsyncSession = Depends(get_db)):
    return await create_user(db, user)

@router.get("/users/{user_id}", response_model=User)
async def read_user(user_id: int, db: AsyncSession = Depends(get_db)):
    db_user = await get_user_by_nfc_data(db, user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
