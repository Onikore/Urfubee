from sqlalchemy import Integer, Column, ForeignKey

from app.db.base_class import Base


class Followers(Base):
    id = Column(Integer(), primary_key=True, unique=True, autoincrement=True)
    subscriber_from = Column(Integer(), ForeignKey("user.id"), nullable=False)
    subscribed_to = Column(Integer(), ForeignKey("user.id"), nullable=False)
