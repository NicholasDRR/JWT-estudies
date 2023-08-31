from fastapi import FastAPI

from app.routes import user_router as router_user
from app.routes import test_router as test_router

app = FastAPI()

app.include_router(router=router_user)
app.include_router(router=test_router)