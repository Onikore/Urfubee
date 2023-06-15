from sqlalchemy import Integer, Column, ForeignKey, Boolean

from app.db.base_class import Base


class Views(Base):
    video_id = Column(Integer(), ForeignKey("video.id"), primary_key=True, nullable=False)
    user_id = Column(Integer(), ForeignKey("user.id"), primary_key=True, nullable=False)
