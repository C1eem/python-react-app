from authx import TokenPayload
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from src.auth.jwt import security
from src.auth.schemas import LoginInDTO, TokenPair, UserAddDTO, UserResponseDTO
from src.auth.service import login_user, register_user
from src.core.database import get_db

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post(
    "/register", response_model=UserResponseDTO, status_code=status.HTTP_201_CREATED
)
async def register(data: UserAddDTO, db: AsyncSession = Depends(get_db)):
    return await register_user(data, db)


@router.post("/login", response_model=TokenPair)
async def login(data: LoginInDTO, db: AsyncSession = Depends(get_db)):
    return await login_user(data, db)


@router.post("/refresh", response_model=dict)
async def refresh(payload: TokenPayload = Depends(security.refresh_token_required)):
    new_access = security.create_access_token(uid=payload.sub)
    return {"access_token": new_access, "token_type": "baerer"}
