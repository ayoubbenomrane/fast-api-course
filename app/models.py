from .database import Base
from sqlalchemy import Column,Integer,String,Float
class Employees(Base):
    __tablename__= "tttt"
    id = Column(Integer, primary_key=True, nullable=False)
    firstName=Column(String, nullable=False)
    lastName=Column(String, nullable=False)
    salary=Column(Float, nullable=True)
