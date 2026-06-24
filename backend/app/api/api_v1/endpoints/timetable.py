from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.timetable import TimetableSlotCreate, TimetableSlotRead
from app.db.session import get_db
from app.crud.timetable import create_timetable_slot, get_timetable_slots, get_timetable_slot
from app.api.dependencies import get_current_user

router = APIRouter()

@router.post("/", response_model=TimetableSlotRead, dependencies=[Depends(get_current_user)])
def create_slot(slot_in: TimetableSlotCreate, db: Session = Depends(get_db)):
    return create_timetable_slot(db, slot_in)

@router.get("/", response_model=list[TimetableSlotRead], dependencies=[Depends(get_current_user)])
def list_slots(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_timetable_slots(db, skip=skip, limit=limit)

@router.get("/{slot_id}", response_model=TimetableSlotRead, dependencies=[Depends(get_current_user)])
def read_slot(slot_id: int, db: Session = Depends(get_db)):
    slot = get_timetable_slot(db, slot_id)
    if not slot:
        raise HTTPException(status_code=404, detail="Timetable slot not found")
    return slot
