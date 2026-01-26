from pydantic import BaseModel
from typing import Optional

class DriverCreate(BaseModel):
    name: str
    email: str
    phone: str
    car_model: str
    car_plate: str

class DriverResponse(DriverCreate):
    id: int