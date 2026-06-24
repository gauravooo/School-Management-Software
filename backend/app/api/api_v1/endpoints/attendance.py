from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.attendance import AttendanceCreate, AttendanceRead
from app.db.session import get_db
from app.crud.attendance import create_attendance, get_attendance_records, get_attendance
from app.api.dependencies import get_current_user

router = APIRouter()

@router.post("/", response_model=AttendanceRead, dependencies=[Depends(get_current_user)])
def create_attendance_record(attendance_in: AttendanceCreate, db: Session = Depends(get_db)):
    return create_attendance(db, attendance_in)

@router.get("/", response_model=list[AttendanceRead], dependencies=[Depends(get_current_user)])
def get_attendance_list(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_attendance_records(db, skip=skip, limit=limit)

@router.get("/{attendance_id}", response_model=AttendanceRead, dependencies=[Depends(get_current_user)])
def read_attendance(attendance_id: int, db: Session = Depends(get_db)):
    attendance = get_attendance(db, attendance_id)
    if not attendance:
        raise HTTPException(status_code=404, detail="Attendance record not found")
    return attendance
