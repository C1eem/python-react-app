from authx import TokenPayload
from fastapi import APIRouter, Depends, Response, status
from sqlalchemy.ext.asyncio import AsyncSession
from src.auth.jwt import security
from src.auth.schemas import LoginInDTO, TokenPair
from src.auth.service import login_user, refresh_user_token
from src.core.database import get_db
from src.users.schemas import UserAddDTO, UserResponseDTO
from src.users.service import create_user_service

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/register", response_model=UserResponseDTO, status_code=201)
async def register(data: UserAddDTO, db: AsyncSession = Depends(get_db)):
    return await create_user_service(data, db)


@router.post("/login", response_model=TokenPair)
async def login(
    response: Response,
    data: LoginInDTO,
    db: AsyncSession = Depends(get_db),
):
    tokens = await login_user(data, db)
    security.set_access_cookies(tokens.access_token, response)
    security.set_refresh_cookies(tokens.refresh_token, response)
    return tokens


@router.post("/refresh", response_model=TokenPair)
async def refresh(
    response: Response,
    payload: TokenPayload = Depends(security.refresh_token_required),
    db: AsyncSession = Depends(get_db),
):
    tokens = await refresh_user_token(payload, db)
    security.set_access_cookies(tokens.access_token, response)
    security.set_refresh_cookies(tokens.refresh_token, response)
    return tokens


@router.post("/logout")
async def logout(response: Response):
    security.unset_access_cookies(response)
    security.unset_refresh_cookies(response)
    return {"detail": "Logged out"}
