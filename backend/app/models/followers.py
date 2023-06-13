from sqlalchemy import Integer, Column, ForeignKey

from app.db.base_class import Base


class Followers(Base):
    id = Column(Integer(), primary_key=True, unique=True, autoincrement=True)
    follower_id = Column(Integer(), ForeignKey("user.id"), nullable=False)
    followed_id = Column(Integer(), ForeignKey("user.id"), nullable=False)
