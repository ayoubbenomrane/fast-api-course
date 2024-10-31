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

try:
    conn=psycopg2.connect(host='localhost' , database='fastapi',user='postgres', password='Ayoub2003', cursor_factory=RealDictCursor)
    cursor=conn.cursor()
    print('database conencted succesefully')
except Exception as error:
    print("Error: ", error)


@app.get("/employees")
def test_posts(db: Session = Depends(get_db)):
    employees= db.query(models.Employees).all()
    return {"data" : employees}

@app.post("/employees")
def create_employee(employee:Employee,db:Session=Depends(get_db)):
    new_employee=models.Employees(
         firstName=employee.firstName, lastName=employee.lastName, salary=employee.salary
    )
    db.add(new_employee)
    db.commit()
    db.refresh(new_employee)
    return{"data": new_employee}