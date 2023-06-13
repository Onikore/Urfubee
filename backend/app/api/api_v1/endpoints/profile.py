from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import crud
from app.api import deps
from app.models.user import User
from app.schemas.user import UserInDB, UserUpdate

router = APIRouter()


@router.get('/', response_model=UserInDB)
def read_profile(current_user: User = Depends(deps.get_current_user)) -> User:
    return current_user


@router.put('/', response_model=UserInDB)
def update_profile(data: UserUpdate,
                   db: Session = Depends(deps.get_db),
                   current_user: User = Depends(deps.get_current_user),
                   ) -> User:
    user = crud.user.update(db, db_obj=current_user, obj_in=data)
    return user
