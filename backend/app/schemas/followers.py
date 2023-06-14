from pydantic import BaseModel


class FollowerBase(BaseModel):
    subscriber_from: int = None
    subscribed_to: int = None


class FollowerCreate(FollowerBase):
    subscribed_to: int


class FollowerUpdate(FollowerBase):
    ...


class LikeInDB(FollowerBase):
    id: int

    class Config:
        orm_mode = True
