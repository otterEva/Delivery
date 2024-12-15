from fastapi import FastAPI
from app.api.route_router import router as route_router

app = FastAPI(title="Logistics Platform")

app.include_router(route_router, prefix="/api", tags=["routes"])
