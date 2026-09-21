from pydantic import BaseModel, ConfigDict
from src.users.models import UserRole


class UserAddDTO(BaseModel):
    email: str
    password: str
    first_name: str
    last_name: str
    middle_name: str | None


class UserCreateInDB(BaseModel):
    email: str
    hashed_password: str
    first_name: str
    last_name: str
    middle_name: str | None
    role: UserRole = UserRole.parent  # роль по умолчанию


class UserResponseDTO(BaseModel):
    id: int
    email: str
    first_name: str
    last_name: str
    middle_name: str | None
    role: UserRole

    model_config = ConfigDict(from_attributes=True)
