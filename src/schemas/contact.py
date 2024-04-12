from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr, Field, ConfigDict

from src.schemas.user import UserResponse


class ContactSchema(BaseModel):
    first_name: str = Field(min_length=3, max_length=20)
    last_name: str = Field(min_length=3, max_length=20)
    email: EmailStr = Field(min_length=3, max_length=40)
    phone_number: str = Field(max_length=20)
    birthday: str = Field(max_length=20)
    extra_info: str = Field(min_length=3, max_length=250)
    completed: Optional[bool] = False


class ContactUpdateSchema(ContactSchema):
    first_name: Optional[str] = Field(None, min_length=3, max_length=20)
    last_name: Optional[str] = Field(None, min_length=3, max_length=20)
    email: Optional[EmailStr] = Field(None, min_length=3, max_length=40)
    phone_number: Optional[str] = Field(None, max_length=20)
    birthday: Optional[str] = Field(None, max_length=20)  # Теж використовуємо str для строки
    extra_info: Optional[str] = Field(None, min_length=3, max_length=250)
    completed: bool


class ContactResponse(BaseModel):
    id: int = 1
    first_name: str
    last_name: str
    email: str
    phone_number: str
    birthday: str
    extra_info: str
    completed: bool
    created_at: datetime | None
    updated_at: datetime | None
    user: UserResponse | None
    model_config = ConfigDict(from_attributes = True)  # noqa
    # user: UserRead | None



class ContactSearchSchema(BaseModel):
    first_name: str
