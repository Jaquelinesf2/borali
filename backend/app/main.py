from fastapi import FastAPI
from app.routes import health

app = FastAPI(
    title="Borali API",
    description="API do aplicativo de transporte estilo Uber",
    version="0.1.0"
)

API_V1_PREFIX = "/api/v1"

app.include_router(
    health.router,
    prefix=API_V1_PREFIX
)
