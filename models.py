from .database import Base
from sqlalchemy import Column,Integer,String,Float
class Post(Base):
    __tablename__= "employees"
    id = Column(Integer, primary_key=True, nullable=False)
    firstName=Column(String, nullable=False)
    lasName=Column(String, nullable=False)
    salary=Column(Float, nullable=True)
