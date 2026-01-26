from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.driver import DriverCreate, DriverResponse
from app.models.driver import Driver
from app.dependencies import get_db

router = APIRouter(
    prefix="/drivers",
    tags=["Drivers"]
)

@router.post("/", response_model=DriverResponse)
def create_driver(driver: DriverCreate, db: Session = Depends(get_db)):
    new_driver = Driver(**driver.dict())
    db.add(new_driver)
    db.commit()
    db.refresh(new_driver)
    return new_driver


@router.get("/", response_model=list[DriverResponse])
def list_drivers(db: Session = Depends(get_db)):
    return db.query(Driver).all()