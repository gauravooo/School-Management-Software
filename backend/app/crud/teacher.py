from sqlalchemy.orm import Session
from app.models.teacher import Teacher
from app.schemas.teacher import TeacherCreate


def get_teacher(db: Session, teacher_id: int) -> Teacher | None:
    return db.query(Teacher).filter(Teacher.id == teacher_id).first()


def get_teachers(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Teacher).offset(skip).limit(limit).all()


def create_teacher(db: Session, teacher_in: TeacherCreate) -> Teacher:
    teacher = Teacher(**teacher_in.dict())
    db.add(teacher)
    db.commit()
    db.refresh(teacher)
    return teacher


def bulk_create_teachers(db: Session, teachers: list[TeacherCreate]) -> tuple[list[Teacher], list[dict]]:
    """
    Bulk create teachers from CSV data.
    Returns: (created_teachers, errors)
    """
    created_teachers = []
    errors = []
    
    for idx, teacher_in in enumerate(teachers):
        try:
            teacher = Teacher(**teacher_in.dict())
            db.add(teacher)
            created_teachers.append(teacher)
        except Exception as e:
            errors.append({
                "row": idx + 2,
                "error": str(e),
                "data": teacher_in.dict()
            })
    
    try:
        db.commit()
        for teacher in created_teachers:
            db.refresh(teacher)
    except Exception as e:
        db.rollback()
        errors.append({
            "row": "all",
            "error": f"Failed to save to database: {str(e)}"
        })
        created_teachers = []
    
    return created_teachers, errors
