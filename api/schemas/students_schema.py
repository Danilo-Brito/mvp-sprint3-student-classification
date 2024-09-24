from pydantic import BaseModel
from typing import Optional, List
from model.student import Student


class StudentSchema(BaseModel):
    """ Define como um novo estudante a ser inserido deve ser representado
    """
    name: str = "Bacate"
    gender: int = 1
    attendance_rate: int = 85
    study_hours_per_week: int = 15
    previous_grade: int = 78
    extracurricular_activities: int = 1
    parental_support: int = 2


class StudentViewSchema(BaseModel):
    """Define como um estudante será retornado
    """
    id: int = 1
    name: str = "Bacate"
    gender: int = 1
    attendance_rate: int = 85
    study_hours_per_week: int = 15
    previous_grade: int = 78
    extracurricular_activities: int = 1
    parental_support: int = 2
    final_grade: int = None


class StudentSearchSchema(BaseModel):
    """Define como deve ser a estrutura que representa a busca.
    Ela será feita com base no nome do estudante.
    """
    name: str = "Bacate"


def show_single_student(student: Student):
    """ Retorna uma representação do estudante seguindo o schema definido em
        StudentViewSchema.
    """
    return {
        "id": student.id,
        "name": student.name,
        "gender": student.gender,
        "attendance_rate": student.attendance_rate,
        "study_hours_per_week": student.study_hours_per_week,
        "previous_grade": student.previous_grade,
        "extracurricular_activities": student.extracurricular_activities,
        "parental_support": student.parental_support,
        "final_grade": student.final_grade,
    }


def show_students(students: List[Student]):
    """ Retorna uma representação do estudante seguindo o schema definido em
        StudentViewSchema.
    """
    result = []
    for student in students:
        result.append({
            "id": student.id,
            "name": student.name,
            "gender": student.gender,
            "attendance_rate": student.attendance_rate,
            "study_hours_per_week": student.study_hours_per_week,
            "previous_grade": student.previous_grade,
            "extracurricular_activities": student.extracurricular_activities,
            "parental_support": student.parental_support,
            "final_grade": student.final_grade,
        })

    return {"students": result}
