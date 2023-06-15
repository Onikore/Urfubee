from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status

from app import crud
from app.api import deps
from app.models.user import User
from app.schemas.video import VideoInDB, VideoCreate

router = APIRouter()


@router.get('/', response_model=List[VideoInDB])
def get_multi_videos(skip=0, limit=5, db: Session = Depends(deps.get_db)) -> List[VideoInDB]:
    return crud.video.get_multi(db, skip=skip, limit=limit)


@router.post('/')
def create_video(obj_in: VideoCreate,
                 current_user: User = Depends(deps.get_current_user),
                 db: Session = Depends(deps.get_db)):
    obj_in.user_id = current_user.id
    return crud.video.create(db, obj_in=obj_in)


@router.get('/{id}', response_model=VideoInDB)
def get_video(id: int, db: Session = Depends(deps.get_db)) -> VideoInDB:
    video = crud.video.get(db, id=id)
    if not video:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Video not found")
    return video
