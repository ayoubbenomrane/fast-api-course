from typing import List
from fastapi import FastAPI, HTTPException,status,Depends
from pydantic import BaseModel
from fastapi.params import Body
import psycopg2 ,time
from psycopg2.extras import RealDictCursor
from . import models,schemas
from sqlalchemy.orm import Session
from .database import engine,SessionLocal,get_db
from passlib.context import CryptContext
models.Base.metadata.create_all(bind=engine)
pwd_context = CryptContext(schemes=["bcrypt"],deprecated="auto")
app = FastAPI()





@app.get("/employees",response_model=List[schemas.Employee])
def get_employee(db: Session = Depends(get_db)):
    employees= db.query(models.Employees).all()
    return employees

@app.post("/employees")
def create_employee(employee:schemas.EmployeeBase,db:Session=Depends(get_db)):
    test=employee.model_dump()
    print(test)
    new_employee=models.Employees(**employee.model_dump())
    db.add(new_employee)
    db.commit()
    db.refresh(new_employee)
    return{"data": new_employee}


@app.get("/employees/{id}")
def get_employee(id:int, db: Session = Depends(get_db)):
    employee= db.query(models.Employees).filter(models.Employees.id==id).first()
    if not employee:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with id {id} doesn\'t exit")
    return {"data" : employee}

@app.delete("/employees/{id}")
def get_employee(id:int, db: Session = Depends(get_db)):
    employee= db.query(models.Employees).filter(models.Employees.id==id)
    if employee.first()==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with id {id} doesn\'t exit")
    employee.delete(synchronize_session=False)
    db.commit()
    return {"employee deleted":employee}

@app.put("/employees/{id}")
def update_employee(id:int,employee:schemas.EmployeeBase, db:Session=Depends(get_db)):
    employee_query=db.query(models.Employees).filter(models.Employees.id==id)
    if employee_query.first()==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with id {id} doesn\'t exit")
    employee_query.update(employee.model_dump(),synchronize_session=False)
    
    db.commit()
