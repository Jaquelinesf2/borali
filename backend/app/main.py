from fastapi import FastAPI

from app.core.config import settings
from app.routes import health

app = FastAPI(
    title=settings.APP_NAME,
    description=settings.APP_DESCRIPTION,
    version=settings.APP_VERSION
)

app.include_router(
    health.router,
    prefix=settings.API_V1_PREFIX
)
