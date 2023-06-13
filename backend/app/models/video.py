import datetime

from sqlalchemy import Integer, Column, String, DateTime
from sqlalchemy.orm import relationship

from app.core.config import settings
from app.db.base_class import Base


class Video(Base):
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True, index=True)
    name = Column(String(), nullable=False)
    url = Column(String(), nullable=False)
    s3_url = Column(String(), nullable=False)
    preview_url = Column(String(), default=settings.DEFAULT_PREVIEW)
    description = Column(String())
    created_at = Column(DateTime(), default=datetime.datetime.utcnow())
    likes = relationship('Likes', backref='likes')
    comments = relationship('Comments', backref='comments')
