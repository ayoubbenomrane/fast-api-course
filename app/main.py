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
print("aaa")


class Employee(BaseModel):
    name: str
    position: str
    salary: float

try:
    conn=psycopg2.connect(host='localhost' , database='fastapi',user='postgres', password='Ayoub2003', cursor_factory=RealDictCursor)
    cursor=conn.cursor()
    print('database conencted succesefully')
except Exception as error:
    print("Error: ", error)
@app.get("/")
def get_posts():
    cursor.execute("""SELECT * FROM employees""" )
    
    posts=cursor.fetchall()
    print(5)
    print(posts)
    conn.commit()
    return {"data":posts}
    
@app.get("/sqlalchemy")
def test_posts(db: Session = Depends(get_db)):
    employees= db.query(models.employees).all()
    return {"data" : employees}

@app.post("/")
def create_employee(employee:Employee):
    cursor.execute("""INSERT INTO employees (name,position,salary) VALUES (%s, %s,%s)""" , (employee.name,employee.position, employee.salary))
    post=cursor.fetchone()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,)
    return "employee added succesully"

    
