from fastapi import FastAPI

from src.routers.routerBarber import router
from src.database.config.connect import create_all

create_all()

app = FastAPI()

app.include_router(router)