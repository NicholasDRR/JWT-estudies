from sqlalchemy import Column, Integer, String
from app.db import Base


class UserModel(Base):
    __tablename__ = "users"
    id = Column('int', Integer, primary_key=True, nullable=False, autoincrement=True)
    username = Column('str', String, nullable=False, unique=True)
    password = Column('str', String, nullable=False)