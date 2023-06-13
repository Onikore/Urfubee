import datetime

from pydantic import BaseModel


class CommentBase(BaseModel):
    user_id: int = None
    text: str = None
    created_at: datetime.datetime = None


class GetComments(CommentBase):
    ...


class CommentCreate(CommentBase):
    video_id: int
    user_id: int
    text: str


class CommentInDB(CommentBase):
    created_at: datetime.datetime

    class Config:
        orm_mode = True
