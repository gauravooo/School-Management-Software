from sqlalchemy.orm import Session
from app.models.classroom import Classroom
from app.schemas.classroom import ClassroomCreate


def get_classroom(db: Session, classroom_id: int) -> Classroom | None:
    return db.query(Classroom).filter(Classroom.id == classroom_id).first()


def get_classrooms(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Classroom).offset(skip).limit(limit).all()


def create_classroom(db: Session, classroom_in: ClassroomCreate) -> Classroom:
    classroom = Classroom(**classroom_in.dict())
    db.add(classroom)
    db.commit()
    db.refresh(classroom)
    return classroom
