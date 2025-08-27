from base import Base
from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    String,
)
from pydantic import BaseModel

class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)

class Book(Base):
    __tablename__ = "book"
    id = Column(Integer, primary_key=True, autoincrement=True)
    book_name = Column(String, nullable=False)
    cover = Column(String)

class Reading_log(Base):
    __tablename__ = "reading_log"
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    book_id = Column(Integer, ForeignKey("book.id"), nullable=False)
    chapter = Column(Integer)
    chapter_notes = Column(String)


class ReadingRecord(BaseModel):
    user_id: int
    book_id: int
    chapter: int
    chapter_notes: str