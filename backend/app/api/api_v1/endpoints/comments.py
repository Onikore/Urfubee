from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import crud
from app.api import deps
from app.models.user import User
from app.schemas.comment import GetComments, CommentInDB, CommentCreate

router = APIRouter()


@router.get('/{video_id}', response_model=List[GetComments])
async def read_comments(video_id: int, skip=0, limit=5, db: Session = Depends(deps.get_db)):
    return crud.comments.get_multi_com(db=db, video_id=video_id, skip=skip, limit=limit)


@router.post('/{video_id}', response_model=CommentInDB)
async def create_comment(obj_in: CommentCreate,
                         current_user: User = Depends(deps.get_current_user),
                         db: Session = Depends(deps.get_db)):
    obj_in.user_id = current_user.id
    return crud.comments.create(db, obj_in=obj_in)
