import datetime

from pydantic import BaseModel


class VideoBase(BaseModel):
    name: str = None
    url: str = None
    s3_url: str = None
    preview_url: str = None
    description: str = None
    created_at: datetime.datetime = None


class VideoCreate(VideoBase):
    ...


class VideoUpdate(VideoBase):
    ...


class VideoInDB(VideoBase):
    id: int

    class Config:
        orm_mode = True
