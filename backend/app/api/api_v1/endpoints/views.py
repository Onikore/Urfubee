from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import crud
from app.api import deps
from app.models.user import User
from app.schemas.views import ViewsCreate

router = APIRouter()


@router.post('/')
def see_video(obj_in: ViewsCreate,
              current_user: User = Depends(deps.get_current_user),
              db: Session = Depends(deps.get_db)):
    obj_in.user_id = current_user.id
    return crud.views.create(db, obj_in=obj_in)


@router.get('/{video_id}')
def views_count(video_id: int,
                db: Session = Depends(deps.get_db)):
    return crud.views.get_video_views(db, video_id=video_id)
