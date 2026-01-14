from sqlalchemy.orm import Session
from .. import models, schema
from fastapi import Depends
from fastapi import HTTPException, status, Response
from ..hashing import Hash


def create(request: schema.User, db: Session):
    #hashedPassword = pwd_cxt.hash(request.password)
    new_user = models.User(name=request.name, email=request.email, password=Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get(id: int, db: Session):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="User not found")
    
    return user
