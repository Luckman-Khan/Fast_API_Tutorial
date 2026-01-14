from sqlalchemy.orm import Session
from .. import models, schema
from fastapi import Depends
from ..database import get_db
from fastapi import HTTPException, status, Response


def get_all(db:Session):
    blogs = db.query(models.Blog).all()
    return blogs

def create(request: schema.Blog, db: Session):

    new_Blog = models.Blog(title=request.title, body=request.body, user_id= 1)
    db.add(new_Blog)
    db.commit()
    db.refresh(new_Blog)
    return new_Blog

def destroy(id: int, db:Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Blog not found")
    db.delete(blog)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

def update(id: int, request: schema.Blog, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if  not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        
    blog.update(request.dict())
    db.commit()
    return "Updated"

def show(id: int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Blog not found")
    return blog