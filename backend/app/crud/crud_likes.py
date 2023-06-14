from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.likes import Likes
from app.schemas.likes import LikeCreate, LikeUpdate


class CRUDLike(CRUDBase[Likes, LikeCreate, LikeUpdate]):
    def likes_count(self, db: Session, video_id: int):
        obj = db.query(self.model).filter(self.model.video_id == video_id)
        likes = obj.filter(self.model.like_type == True).count()
        dislikes = obj.filter(self.model.like_type == False).count()
        return {
            'likes': likes,
            'dislikes': dislikes
        }

    def like(self, db: Session, obj_in: LikeCreate):
        like = db.query(self.model) \
            .filter(self.model.user_id == obj_in.user_id) \
            .filter(self.model.video_id == obj_in.video_id).first()

        if not like:
            return super().create(db, obj_in=obj_in)
        swap = like.like_type != obj_in.like_type

        if swap:
            return super().update(db, db_obj=like, obj_in=obj_in)
        else:
            return super().remove(db, obj=like)


likes = CRUDLike(Likes)
