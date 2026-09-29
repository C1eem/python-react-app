from authx import TokenPayload
from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from src.auth.jwt import security
from src.auth.schemas import LoginInDTO, TokenPair
from src.core.security import verify_password
from src.users.service import get_user_by_email, get_user_by_id


async def login_user(user_data: LoginInDTO, db: AsyncSession) -> TokenPair:
    user = await get_user_by_email(user_data.email, db)
    if not user or not verify_password(user_data.password, user.hashed_password):
        raise HTTPException(401, detail="Invalid credentials")
    access = security.create_access_token(uid=str(user.id))
    refresh = security.create_refresh_token(uid=str(user.id))
    return TokenPair(access_token=access, refresh_token=refresh)


async def refresh_user_token(payload: TokenPayload, db: AsyncSession) -> TokenPair:
    user = await get_user_by_id(int(payload.sub), db)
    if not user or not user.is_active:
        raise HTTPException(401, detail="Invalid refresh token")
    access = security.create_access_token(uid=str(user.id))
    refresh = security.create_refresh_token(uid=str(user.id))
    return TokenPair(access_token=access, refresh_token=refresh)
