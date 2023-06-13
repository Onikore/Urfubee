from app.crud.base import CRUDBase
from app.models.video import Video
from app.schemas.video import VideoCreate, VideoUpdate


class CRUDVideo(CRUDBase[Video, VideoCreate, VideoUpdate]):
    ...


video = CRUDVideo(Video)
