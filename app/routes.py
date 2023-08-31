from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordRequestForm

from app.schemas import User
from app.db.depends import get_db_session
from app.auth_user import UserUseCases
from app.db.connection import Session

router = APIRouter(
    prefix="/user"
)

@router.post("/register")
def create_user(user: User, db_session: Session = Depends(get_db_session)):
    
    uc = UserUseCases(db_session)
    uc.user_register(user)
    
    return JSONResponse(content={"msg": "User successfully created!"})



@router.post("/login")
def login_user(request_form_user: OAuth2PasswordRequestForm = Depends(), db_session: Session = Depends(get_db_session)):
    
    uc = UserUseCases(db_session)
    user = User(
        username=request_form_user.username,
        password=request_form_user.password
    )
    
    auth_data = uc.user_login(user)
    return JSONResponse(content=auth_data, status_code=status.HTTP_200_OK)
    