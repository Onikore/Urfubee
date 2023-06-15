from fastapi import APIRouter

from app.api.api_v1.endpoints import auth, profile, video, comments, likes, followers, views

api_router = APIRouter(prefix='/api/v1')
api_router.include_router(auth.router, prefix='/auth', tags=['auth'])
api_router.include_router(profile.router, prefix='/profile', tags=['profile'])
api_router.include_router(video.router, prefix='/video', tags=['video'])
api_router.include_router(comments.router, prefix='/comments', tags=['comments'])
api_router.include_router(likes.router, prefix='/likes', tags=['likes'])
api_router.include_router(followers.router, prefix='/followers', tags=['followers'])
api_router.include_router(views.router, prefix='/views', tags=['views'])
