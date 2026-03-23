from sqlalchemy import Column, Integer, Float, String
from .database import Base


class Address(Base):
    """SQLAlchemy model for address entries."""
    __tablename__ = "addresses"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)