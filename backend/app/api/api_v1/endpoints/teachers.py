from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.teacher import TeacherCreate, TeacherRead
from app.db.session import get_db
from app.crud.teacher import create_teacher, get_teachers, get_teacher
from app.api.dependencies import get_current_user

router = APIRouter()

@router.post("/", response_model=TeacherRead, dependencies=[Depends(get_current_user)])
def create_new_teacher(teacher_in: TeacherCreate, db: Session = Depends(get_db)):
    return create_teacher(db, teacher_in)

@router.get("/", response_model=list[TeacherRead], dependencies=[Depends(get_current_user)])
def list_teachers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_teachers(db, skip=skip, limit=limit)

@router.get("/{teacher_id}", response_model=TeacherRead, dependencies=[Depends(get_current_user)])
def read_teacher(teacher_id: int, db: Session = Depends(get_db)):
    teacher = get_teacher(db, teacher_id)
    if not teacher:
        raise HTTPException(status_code=404, detail="Teacher not found")
    return teacher
