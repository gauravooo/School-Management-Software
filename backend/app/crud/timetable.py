from sqlalchemy.orm import Session
from app.models.timetable import TimetableSlot
from app.schemas.timetable import TimetableSlotCreate


def get_timetable_slot(db: Session, slot_id: int) -> TimetableSlot | None:
    return db.query(TimetableSlot).filter(TimetableSlot.id == slot_id).first()


def get_timetable_slots(db: Session, skip: int = 0, limit: int = 100):
    return db.query(TimetableSlot).offset(skip).limit(limit).all()


def create_timetable_slot(db: Session, slot_in: TimetableSlotCreate) -> TimetableSlot:
    slot = TimetableSlot(**slot_in.dict())
    db.add(slot)
    db.commit()
    db.refresh(slot)
    return slot
