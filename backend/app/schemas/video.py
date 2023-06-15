import datetime

from pydantic import BaseModel


class VideoBase(BaseModel):
    user_id: int = None
    name: str = None
    s3_url: str = None
    preview_url: str = None
    description: str = None
    created_at: datetime.datetime = None


class VideoCreate(VideoBase):
    name: str
    s3_url: str
    preview_url: str
    description: str


class VideoUpdate(VideoBase):
    ...


class VideoInDB(VideoBase):
    id: int

    class Config:
        orm_mode = True
