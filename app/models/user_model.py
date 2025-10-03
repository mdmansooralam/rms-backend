from datetime import datetime
from pydantic import BaseModel, Field, EmailStr
from typing import Optional, Literal
import uuid


class User(BaseModel):
    
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    email: EmailStr
    password: str
    profilePicture: Optional[str] = None
    role: Literal['user', 'admin'] = 'user'
    resetPasswordToken: Optional[str] = None
    resetPasswordExpires: Optional[datetime] = None
    
