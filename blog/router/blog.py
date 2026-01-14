from fastapi import APIRouter
from typing import List
from ..database import SessionLocal, engine
from .. import models
from fastapi import Depends, status, HTTPException
from sqlalchemy.orm import Session
from ..hashing import Hash
from .. import schema, database
from ..database import get_db
from ..repository import blog
from ..router import oauth2
from ..router.oauth2 import get_current_user

router = APIRouter(
    tags = ['Blogs'],
    prefix="/blog"
)


@router.get('/', response_model=List[schema.ShowBlog])
def all(db: Session = Depends(get_db), current_user: schema.User = Depends(get_current_user) ):
    return blog.get_all(db)


@router.get('/{id}',status_code=status.HTTP_200_OK,response_model = schema.ShowBlog )
def show(id, db: Session = Depends(get_db), current_user: schema.User = Depends(get_current_user)   ):
    return blog.show(id, db)


@router.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT )
def destroy(id, db:Session = Depends(get_db), current_user: schema.User = Depends(get_current_user)):
    return blog.destroy(id, db)

@router.put('/{id}',status_code =status.HTTP_202_ACCEPTED)
def update(id, request:schema.Blog, db:Session = Depends(get_db), current_user: schema.User = Depends(get_current_user)):
    return blog.update(id, request, db)

@router.post('/',status_code=status.HTTP_201_CREATED )
def create(request: schema.Blog, db: Session = Depends(get_db), current_user: schema.User = Depends(get_current_user)):
    return blog.create(request, db)


