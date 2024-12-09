from pydantic import BaseModel, EmailStr, Field

class UserCreateSchema(BaseModel):
    username: str = Field(..., max_length=30)
    email: EmailStr
    password: str = Field(..., min_length=6)
    
class UserOutSchema(BaseModel):
    username: str
    email: str
    
    class Config:
        orm_mode = True