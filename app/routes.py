from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List
from geopy.distance import geodesic

from .database import SessionLocal
from . import crud, schemas
from .logger import logger

router = APIRouter(prefix="/api/v1/addresses", tags=["Addresses"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=schemas.AddressOut)
def create_address(address: schemas.AddressCreate, db: Session = Depends(get_db)):
    logger.info(f"Creating address: {address.name}")
    try:
        return crud.create_address(db, address)
    except Exception:
        logger.error("Failed to create address")
        raise HTTPException(status_code=500, detail="Internal server error")


@router.get("/", response_model=List[schemas.AddressOut])
def get_all(db: Session = Depends(get_db)):
    logger.info("Fetching all addresses")
    return crud.get_addresses(db)


@router.put("/{address_id}", response_model=schemas.AddressOut)
def update(address_id: int, data: schemas.AddressCreate, db: Session = Depends(get_db)):
    logger.info(f"Updating address ID: {address_id}")
    result = crud.update_address(db, address_id, data)

    if not result:
        raise HTTPException(status_code=404, detail="Address not found")

    return result


@router.delete("/{address_id}")
def delete(address_id: int, db: Session = Depends(get_db)):
    logger.info(f"Deleting address ID: {address_id}")
    success = crud.delete_address(db, address_id)

    if not success:
        raise HTTPException(status_code=404, detail="Address not found")

    return {"message": "Deleted successfully"}


@router.get("/nearby")
def nearby(
    lat: float = Query(..., ge=-90, le=90),
    lon: float = Query(..., ge=-180, le=180),
    distance_km: float = Query(..., gt=0),
    db: Session = Depends(get_db)
):
    logger.info(f"Searching nearby addresses: lat={lat}, lon={lon}, distance={distance_km}")

    addresses = crud.get_addresses(db)
    result = []

    for addr in addresses:
        dist = geodesic((lat, lon), (addr.latitude, addr.longitude)).km
        if dist <= distance_km:
            result.append({
                "id": addr.id,
                "name": addr.name,
                "latitude": addr.latitude,
                "longitude": addr.longitude,
                "distance_km": round(dist, 2)
            })

    return result