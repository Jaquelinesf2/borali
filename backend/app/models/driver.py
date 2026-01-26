from sqlalchemy import Column, Integer, String
from app.database import Base

class Driver(Base):
    __tablename__ = "drivers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    phone = Column(String, nullable=False)
    car_model = Column(String, nullable=False)
    car_plate = Column(String, nullable=False)