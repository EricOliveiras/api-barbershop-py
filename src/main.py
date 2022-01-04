from fastapi import FastAPI

from src.routers.routerBarber import router_barber
from src.routers.routerClient import router_client
from src.routers.routerService import router_service
from src.routers.routerPayment import router_payment


app = FastAPI()

app.include_router(router_barber)
app.include_router(router_client)
app.include_router(router_service)
app.include_router(router_payment)
