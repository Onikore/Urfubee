from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import crud
from app.api import deps
from app.models.user import User
from app.schemas.followers import FollowerCreate

router = APIRouter()


@router.post('/')
def follow(obj_in: FollowerCreate,
           current_user: User = Depends(deps.get_current_user),
           db: Session = Depends(deps.get_db)):
    obj_in.follower_id = current_user.id
    return crud.followers.follow(db, obj_in=obj_in)


@router.get('/count')
def followers_count(user_id: int,
                    db: Session = Depends(deps.get_db)):
    return crud.followers.get_subscribers_count(db, user_id=user_id)


@router.get('/list')
def followers_list(current_user: User = Depends(deps.get_current_user),
                   db: Session = Depends(deps.get_db)):
    return crud.followers.my_subscribers_list(db, user_id=current_user.id)
