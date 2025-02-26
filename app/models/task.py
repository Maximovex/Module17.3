from app.backend.dp import Base
from sqlalchemy import Column, String, Integer, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from app.models import user


class Task(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    content = Column(String)
    priority = Column(Integer, default=0)
    completed = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    slug=Column(String,unique=True,index=True)

    user=relationship('User',back_populates='tasks')

from sqlalchemy.schema import CreateTable
print(CreateTable(Task.__table__))
