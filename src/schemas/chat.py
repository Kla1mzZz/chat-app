from datetime import datetime
from pydantic import BaseModel

class MessageSendSchema(BaseModel):
    content: str
    user_id: int
    chat_id: int
    
    class Config:
        orm_mode = True

class MessageOutSchema(BaseModel):
    id: int
    content: str
    timestamp: datetime
    user_id: int
    chat_id: int

    class Config:
        orm_mode = True