from fastapi import APIRouter, Depends, HTTPException
from .. import schema
from sqlalchemy.orm import Session
from ..database.models import Vehicle
from datetime import date


router = APIRouter()

@router.get('/check/{chassis}/{libre}')
def check_registration(chassis: str, libre: str, db: Session = Depends(schema.get_db)):
    target_vehicle = db.query(Vehicle).filter_by(chassis=chassis, libre=libre).first()
    return target_vehicle


@router.get('/renewal_date/{chassis}')
def get_renewal_date(chassis: str, db: Session = Depends(schema.get_db)):
    target_vehicle = db.query(Vehicle).filter_by(chassis=chassis).first()
    if target_vehicle:
        return target_vehicle.renewal_date


@router.put("/date_update/{chassis}/{new_date}")
def update_renewal_date(request: schema.Vehicle, chassis: str, new_date: date, db: Session = Depends(schema.get_db)):
    vehicle = db.query(Vehicle).filter_by(chassis=chassis).first()
    if not vehicle:
        raise HTTPException(status_code=404, detail="Vehicle not found")
    vehicle.renewal_date = new_date
    db.add(vehicle)
    db.commit()
    db.refresh(vehicle)
    return vehicle


@router.post("/vehicles/")
def register_vehicle(request: schema.Vehicle, db: Session = Depends(schema.get_db)):
    vehicle = Vehicle(chassis=request.chassis, libre=request.libre, renewal_date=request.renewal_date)
    db.add(vehicle)
    db.commit()
    db.refresh(vehicle)
    return vehicle

