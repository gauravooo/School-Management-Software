from sqlalchemy.orm import Session
from app.models.attendance import AttendanceRecord
from app.schemas.attendance import AttendanceCreate


def get_attendance(db: Session, attendance_id: int) -> AttendanceRecord | None:
    return db.query(AttendanceRecord).filter(AttendanceRecord.id == attendance_id).first()


def get_attendance_records(db: Session, skip: int = 0, limit: int = 100):
    return db.query(AttendanceRecord).offset(skip).limit(limit).all()


def create_attendance(db: Session, attendance_in: AttendanceCreate) -> AttendanceRecord:
    attendance = AttendanceRecord(**attendance_in.dict())
    db.add(attendance)
    db.commit()
    db.refresh(attendance)
    return attendance
