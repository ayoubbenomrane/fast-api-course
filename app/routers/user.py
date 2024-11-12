from .. import models,utils,schemas
from fastapi import FastAPI, HTTPException,status,Depends,APIRouter
from sqlalchemy.orm import Session
from ..database import engine,SessionLocal,get_db

router=APIRouter()

@router.post("/user")
def create_user(user:schemas.UserCreate,db:Session=Depends(get_db)):
    hashed_password=utils.hash(user.password)
    user.password=hashed_password
    db.add(models.User(**user.model_dump()))
    db.commit()
    return {**user.model_dump()}




@router.get("/user/{id}",response_model=schemas.UserOut)
def get_employee(id:int, db: Session = Depends(get_db)):
    user= db.query(models.User).filter(models.User.id==id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with id {id} doesn\'t exit")
    return user
