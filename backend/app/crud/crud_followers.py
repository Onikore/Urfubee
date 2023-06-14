from sqlalchemy.orm import Session, load_only

from app.crud.base import CRUDBase
from app.models.followers import Followers
from app.schemas.followers import FollowerCreate, FollowerUpdate


class CRUDFollower(CRUDBase[Followers, FollowerCreate, FollowerUpdate]):
    def follow(self, db: Session, obj_in: FollowerCreate):
        follow = db.query(self.model) \
            .filter(self.model.subscriber_from == obj_in.subscriber_from) \
            .filter(self.model.subscribed_to == obj_in.subscribed_to).first()
        if not follow:
            return super().create(db, obj_in=obj_in)
        else:
            return super().remove(db, obj=follow)

    def get_subscribers_count(self, db: Session, user_id: int):
        return db.query(self.model).filter(self.model.subscribed_to == user_id).count()

    def my_subscribers_list(self, db: Session, user_id: int):
        return db.query(self.model) \
            .filter(self.model.subscribed_to == user_id) \
            .options(load_only('subscribed_to')).all()


followers = CRUDFollower(Followers)
