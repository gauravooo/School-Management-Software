from sqlalchemy.orm import Session
from app.models.student import Student
from app.schemas.student import StudentCreate


def get_student(db: Session, student_id: int) -> Student | None:
    return db.query(Student).filter(Student.id == student_id).first()


def get_students(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Student).offset(skip).limit(limit).all()


def create_student(db: Session, student_in: StudentCreate) -> Student:
    student = Student(**student_in.dict())
    db.add(student)
    db.commit()
    db.refresh(student)
    return student


def bulk_create_students(db: Session, students: list[StudentCreate]) -> tuple[list[Student], list[dict]]:
    """
    Bulk create students from CSV data.
    Returns: (created_students, errors)
    """
    created_students = []
    errors = []
    
    for idx, student_in in enumerate(students):
        try:
            student = Student(**student_in.dict())
            db.add(student)
            created_students.append(student)
        except Exception as e:
            errors.append({
                "row": idx + 2,  # +2 because header is row 1
                "error": str(e),
                "data": student_in.dict()
            })
    
    try:
        db.commit()
        for student in created_students:
            db.refresh(student)
    except Exception as e:
        db.rollback()
        errors.append({
            "row": "all",
            "error": f"Failed to save to database: {str(e)}"
        })
        created_students = []
    
    return created_students, errors
