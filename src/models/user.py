from sqlalchemy.orm import Mapped, relationship

from db.database import Base

class User(Base):
    __tablename__ = 'user'
    
    username: Mapped[str]
    email: Mapped[str]
    hashed_password: Mapped[str]
    
    messages: Mapped['Message'] = relationship('Message', back_populates='user')