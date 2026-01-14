from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from ..repository import user
from .. import schema

router = APIRouter(
    tags= ['Users'],
    prefix='/user'
)


@router.post('/',response_model=schema.ShowUser)
def create_user(request: schema.User,db: Session = Depends(get_db)):
   return user.create(request, db)

@router.get('/{id}',response_model=schema.ShowUser)
def get_user(id:int, db:Session = Depends(get_db)):
    return user.get(id, db)