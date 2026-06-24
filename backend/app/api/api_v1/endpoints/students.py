from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.student import StudentCreate, StudentRead
from app.db.session import get_db
from app.crud.student import create_student, get_students, get_student
from app.api.dependencies import get_current_user

router = APIRouter()

@router.post("/", response_model=StudentRead, dependencies=[Depends(get_current_user)])
def create_new_student(student_in: StudentCreate, db: Session = Depends(get_db)):
    return create_student(db, student_in)

@router.get("/", response_model=list[StudentRead], dependencies=[Depends(get_current_user)])
def list_students(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_students(db, skip=skip, limit=limit)

@router.get("/{student_id}", response_model=StudentRead, dependencies=[Depends(get_current_user)])
def read_student(student_id: int, db: Session = Depends(get_db)):
    student = get_student(db, student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student
