import datetime

from sqlalchemy import Integer, Column, String, DateTime, ForeignKey

from app.db.base_class import Base


class Comments(Base):
    id = Column(Integer(), primary_key=True, unique=True, autoincrement=True, index=True)
    video_id = Column(Integer(), ForeignKey("video.id"), nullable=False)
    user_id = Column(Integer(), ForeignKey("user.id"), nullable=False)
    text = Column(String(), nullable=False)
    created_at = Column(DateTime(), default=datetime.datetime.utcnow())
