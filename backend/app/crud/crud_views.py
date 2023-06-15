from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.views import Views
from app.schemas.views import ViewsCreate, ViewsUpdate


class CRUDViews(CRUDBase[Views, ViewsCreate, ViewsUpdate]):
    def create(self, db: Session, *, obj_in: ViewsCreate) -> Views:
        view = db.query(self.model) \
            .filter(self.model.user_id == obj_in.user_id) \
            .filter(self.model.video_id == obj_in.video_id).first()
        if view:
            return view
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_video_views(self, db: Session, video_id: int):
        return db.query(self.model).filter(self.model.video_id == video_id).count()


views = CRUDViews(Views)
