from pydantic import BaseModel,EmailStr


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
class UserOut(BaseModel):
    email:EmailStr


