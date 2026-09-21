from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from src.core.database import get_db
from src.users.schemas import UserAddDTO, UserResponseDTO
from src.users.service import create_user_service

router = APIRouter(prefix="/users", tags=["users"])


@router.post("", response_model=UserResponseDTO)
async def create_user(new_user: UserAddDTO, db: AsyncSession = Depends(get_db)):
    return await create_user_service(new_user, db)
