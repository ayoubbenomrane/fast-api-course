from .. import models,utils,schemas
from fastapi import FastAPI, HTTPException,status,Depends,APIRouter
from sqlalchemy.orm import Session
from ..database import engine,SessionLocal,get_db

router=APIRouter()

@router.post("/employees")
def create_employee(employee:schemas.EmployeeBase,db:Session=Depends(get_db)):
    new_employee=models.Employees(**employee.model_dump())
    db.add(new_employee)
    db.commit()
    db.refresh(new_employee)
    return{"data": new_employee}


@router.get("/employees/{id}")
def get_employee(id:int, db: Session = Depends(get_db)):
    employee= db.query(models.Employees).filter(models.Employees.id==id).first()
    if not employee:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with id {id} doesn\'t exit")
    return {"data" : employee}

@router.delete("/employees/{id}")
def get_employee(id:int, db: Session = Depends(get_db)):
    employee= db.query(models.Employees).filter(models.Employees.id==id)
    if employee.first()==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with id {id} doesn\'t exit")
    employee.delete(synchronize_session=False)
    db.commit()
    return {"employee deleted":employee}

@router.put("/employees/{id}")
def update_employee(id:int,employee:schemas.EmployeeBase, db:Session=Depends(get_db)):
    employee_query=db.query(models.Employees).filter(models.Employees.id==id)
    if employee_query.first()==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with id {id} doesn\'t exit")
    employee_query.update(employee.model_dump(),synchronize_session=False)
    
    db.commit()




@router.get("/employees",response_model=List[schemas.Employee])
def get_employee(db: Session = Depends(get_db)):
    employees= db.query(models.Employees).all()
    return employees
