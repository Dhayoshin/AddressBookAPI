from pydantic import BaseModel, Field


class AddressBase(BaseModel):
    """Base schema for address data with validation."""
    name: str = Field(..., min_length=1, max_length=100)
    latitude: float = Field(..., ge=-90, le=90)
    longitude: float = Field(..., ge=-180, le=180)


class AddressCreate(AddressBase):
    """Schema for creating new addresses."""
    pass


class AddressOut(AddressBase):
    """Schema for address responses including ID."""
    id: int

    class Config:
        from_attributes = True