from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.classroom import ClassroomCreate, ClassroomRead
from app.db.session import get_db
from app.crud.classroom import create_classroom, get_classrooms, get_classroom
from app.api.dependencies import get_current_user, require_role

router = APIRouter()

@router.post("/", response_model=ClassroomRead, dependencies=[Depends(require_role("principal"))])
def create_new_classroom(classroom_in: ClassroomCreate, db: Session = Depends(get_db)):
    return create_classroom(db, classroom_in)

@router.get("/", response_model=list[ClassroomRead], dependencies=[Depends(get_current_user)])
def list_classrooms(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_classrooms(db, skip=skip, limit=limit)

@router.get("/{classroom_id}", response_model=ClassroomRead, dependencies=[Depends(get_current_user)])
def read_classroom(classroom_id: int, db: Session = Depends(get_db)):
    classroom = get_classroom(db, classroom_id)
    if not classroom:
        raise HTTPException(status_code=404, detail="Classroom not found")
    return classroom
