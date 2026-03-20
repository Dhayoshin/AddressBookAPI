from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from typing import List, Optional
from . import models, schemas

def create_address(db: Session, address: schemas.AddressCreate) -> models.Address:
    try:
        db_address = models.Address(**address.dict())
        db.add(db_address)
        db.commit()
        db.refresh(db_address)
        return db_address
    except SQLAlchemyError:
        db.rollback()
        raise

def get_addresses(db: Session) -> List[models.Address]:
    return db.query(models.Address).all()

def get_address(db: Session, address_id: int) -> Optional[models.Address]:
    return db.query(models.Address).filter(models.Address.id == address_id).first()

def update_address(db: Session, address_id: int, data: schemas.AddressCreate) -> Optional[models.Address]:
    address = get_address(db, address_id)
    if not address:
        return None

    try:
        for key, value in data.dict().items():
            setattr(address, key, value)
        db.commit()
        db.refresh(address)
        return address
    except SQLAlchemyError:
        db.rollback()
        raise

def delete_address(db: Session, address_id: int) -> bool:
    address = get_address(db, address_id)
    if not address:
        return False

    try:
        db.delete(address)
        db.commit()
        return True
    except SQLAlchemyError:
        db.rollback()
        raise