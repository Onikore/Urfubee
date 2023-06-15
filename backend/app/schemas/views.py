from pydantic import BaseModel


class ViewsBase(BaseModel):
    video_id: int = None
    user_id: int = None


class ViewsCreate(ViewsBase):
    video_id: int


class ViewsUpdate(ViewsBase):
    ...


class ViewsInDB(ViewsBase):

    class Config:
        orm_mode = True
