from fastapi import HTTPException
from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession
from src.users.models import UserORM
from src.users.schemas import UserAddDTO, UserCreateInDB


async def _get_user_by_email(email: str, db: AsyncSession):
    res = await db.execute(select(UserORM).where(UserORM.email == email))
    return res.scalar_one_or_none()


async def create_user_service(user_data: UserAddDTO, db: AsyncSession):
    if await _get_user_by_email(user_data.email, db):
        raise HTTPException(status_code=400, detail="Email already registered")
    user_in_db = UserCreateInDB(
        email=user_data.email,
        hashed_password=user_data.password,
        first_name=user_data.first_name,
        last_name=user_data.last_name,
        middle_name=user_data.middle_name,
    )
    stmt = insert(UserORM).values(**user_in_db.model_dump()).returning(UserORM)
    res = await db.execute(stmt)
    await db.commit()
    return res.scalar_one()
