from fastapi import FastAPI

from src.routers.routerBarber import router

app = FastAPI()

app.include_router(router)