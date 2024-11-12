from pydantic import BaseModel,EmailStr
from datetime import datetime



class EmployeeBase(BaseModel):
    firstName: str
    lastName: str
    salary: float

class Employee(BaseModel):
    salary:int
    class Config:
        orm_mode=True


class UserCreate(BaseModel):
    email:EmailStr
    password: str
    class Config:
        orm_mode=True
class UserOut(BaseModel):
    id:int
    email:EmailStr
    created_at: datetime
    class Config:
        orm_mode=True


