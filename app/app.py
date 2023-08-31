from fastapi import FastAPI

from app.routes import router as router_user

app = FastAPI()

app.include_router(router=router_user)