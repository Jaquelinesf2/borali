from fastapi import FastAPI
from app.database import engine, Base
from app.routes.health import router as health_router
from app.routes.drivers import router as drivers_router

#Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Borali API",
    version="0.1.0"
)

app.include_router(health_router)
app.include_router(drivers_router)