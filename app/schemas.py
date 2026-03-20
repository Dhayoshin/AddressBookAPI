from pydantic import BaseModel, Field

class AddressBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    latitude: float = Field(..., ge=-90, le=90)
    longitude: float = Field(..., ge=-180, le=180)

class AddressCreate(AddressBase):
    pass

class AddressOut(AddressBase):
    id: int

    class Config:
        from_attributes = True