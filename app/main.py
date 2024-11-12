from typing import List
from fastapi import FastAPI, HTTPException,status,Depends
from pydantic import BaseModel
from fastapi.params import Body
import psycopg2 ,time
from psycopg2.extras import RealDictCursor
from . import models,schemas,utils
from sqlalchemy.orm import Session
from .database import engine,SessionLocal,get_db
from .routers import employee, user 
models.Base.metadata.create_all(bind=engine)
app = FastAPI()


app.include_router(user.router)
app.include_router(employee.router)





