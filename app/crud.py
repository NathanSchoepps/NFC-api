from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models import User
from app.schemas import UserCreate

async def get_user_by_nfc_data(db: AsyncSession, nfc_data: str):
    result = await db.execute(select(User).where(User.nfc_data == nfc_data))
    return result.scalars().first()

async def create_user(db: AsyncSession, user: UserCreate):
    db_user = User(name=user.name, nfc_data=user.nfc_data)
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    return db_user
