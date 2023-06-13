from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import crud
from app.api import deps
from app.models.user import User
from app.schemas.likes import LikeCreate

router = APIRouter()


@router.post('/')
def like_video(obj_in: LikeCreate,
               current_user: User = Depends(deps.get_current_user),
               db: Session = Depends(deps.get_db)):
    obj_in.user_id = current_user.id
    is_liked = crud.likes.like(db, obj_in=obj_in)
    return is_liked
