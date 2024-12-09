from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import DateTime, ForeignKey

from db.database import Base

class Message(Base):
    __tablename__ = 'message'
    
    content: Mapped[str]
    timestamp: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    
    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'))
    user: Mapped['User'] = relationship('User', back_populates='messages')
    
    chat_id: Mapped[int] = mapped_column(ForeignKey('chat.id'))
    chat: Mapped['Chat'] = relationship('Chat', back_populates='messages')

class Chat(Base):
    __tablename__ = 'chat'
    
    name: Mapped[str]
    
    messages: Mapped['Message'] = relationship('Message', back_populates='chat')
    