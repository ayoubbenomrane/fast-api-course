from .database import Base
from datetime import datetime
from sqlalchemy import Column,Integer,String,Float,TIMESTAMP
from sqlalchemy.sql.expression import text
class Employees(Base):
    __tablename__= "tttt"
    id = Column(Integer, primary_key=True, nullable=False)
    firstName=Column(String, nullable=False)
    lastName=Column(String, nullable=False)
    salary=Column(Float, nullable=True)


class user(Base):
    __tablename__="users"
    email=Column(String, nullable=False,primary_key=True)
    password=Column(String,nullable=False)
    created_at=Column(TIMESTAMP(timezone=True),server_default=text('now()'))