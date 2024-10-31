from fastapi import FastAPI, HTTPException,status,Depends
from pydantic import BaseModel
from fastapi.params import Body
import psycopg2 ,time
from psycopg2.extras import RealDictCursor
from . import models
from sqlalchemy.orm import Session
from .database import engine,SessionLocal,get_db
models.Base.metadata.create_all(bind=engine)

app = FastAPI()


class Employee(BaseModel):
    firstName: str
    lastName: str
    salary: float




@app.get("/employees")
def get_employee(db: Session = Depends(get_db)):
    employees= db.query(models.Employees).all()
    return {"data" : employees}

@app.post("/employees")
def create_employee(employee:Employee,db:Session=Depends(get_db)):
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
def update_employee(id:int,employee:Employee, db:Session=Depends(get_db)):
    employee_query=db.query(models.Employees).filter(models.Employees.id==id)
    employee_query.update(employee.model_dump(),synchronize_session=False)
    
    db.commit()
