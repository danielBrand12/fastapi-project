from fastapi import APIRouter

from app.api.endpoints import deliver, client
api_router = APIRouter()

api_router.include_router(client.router, prefix="/clients", tags=["clients"])
api_router.include_router(deliver.router, prefix="/deliverys", tags=["deliverys"])