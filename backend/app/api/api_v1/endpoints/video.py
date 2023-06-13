from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud
from app.api import deps
from app.schemas.video import VideoInDB

router = APIRouter()


@router.get('/', response_model=List[VideoInDB])
def get_multi_videos(skip=0, limit=5, db: Session = Depends(deps.get_db)) -> List[VideoInDB]:
    return crud.video.get_multi(db, skip=skip, limit=limit)


@router.post('/')
def create_video():
    return {'пока что хз как ': 'без фронта'}


@router.get('/{id}', response_model=VideoInDB)
def get_video(id: int, db: Session = Depends(deps.get_db)) -> VideoInDB:
    video = crud.video.get(db, id=id)
    if not video:
        raise HTTPException(status_code=404, detail="Video not found")
    return video
