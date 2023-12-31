from pydantic import BaseModel


class LikeBase(BaseModel):
    video_id: int = None
    user_id: int = None
    like_type: bool = None


class LikeCreate(LikeBase):
    video_id: int
    like_type: bool


class LikeUpdate(LikeBase):
    ...


class LikeInDB(LikeBase):

    class Config:
        orm_mode = True
