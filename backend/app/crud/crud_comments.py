from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.comments import Comments
from app.schemas.comment import CommentCreate


class CRUDComments(CRUDBase[Comments, CommentCreate, ...]):
    def get_multi_com(self, video_id: int, db: Session, *, skip: int = 0, limit: int = 100):
        return db.query(Comments).filter(Comments.video_id == video_id).offset(skip).limit(limit).all()


comments = CRUDComments(Comments)
