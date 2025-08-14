from fastapi import APIRouter, Request, Depends, HTTPException, UploadFile,Query, Form
from sqlalchemy.orm import Session
from typing import List,Annotated
import service, models, schemas
from fastapi import Query
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get('/items/')
async def get_items(db: Session = Depends(get_db)):
    try:
        return await service.get_items(db)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

