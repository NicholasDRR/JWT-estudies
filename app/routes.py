from fastapi import APIRouter
from fastapi import Depends
from fastapi.responses import JSONResponse

from app.schemas import User
from app.db.depends import get_db_session
from app.auth_user import UserUseCases
from app.db.connection import Session

router = APIRouter(
    prefix="/user"
)

@router.post("/")
def create_user(user: User, db_session: Session = Depends(get_db_session)):
    
    uc = UserUseCases(db_session)
    uc.user_register(user)
    
    return JSONResponse(content={"msg": "User successfully created!"})