from pydantic import BaseModel
from typing import Optional, List
from model.student import Student


class StudentSchema(BaseModel):
    """ Define como um novo estudante a ser inserido deve ser representado
    """
    name: str = "Bacate"
    gender: str = "Male"
    attendanceRate: int = 85
    studyHoursPerWeek: int = 15
    previousGrade: int = 78
    extracurricularActivities: int = 1
    parentalSupport: str = "High"


class StudentViewSchema(BaseModel):
    """Define como um estudante será retornado
    """
    id: int = 1
    name: str = "Bacate"
    gender: str = "Male"
    attendanceRate: int = 85
    studyHoursPerWeek: int = 15
    previousGrade: int = 78
    extracurricularActivities: int = 1
    parentalSupport: str = "High"
    finalGrade: int = None


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
        "attendanceRate": student.attendanceRate,
        "studyHoursPerWeek": student.studyHoursPerWeek,
        "previousGrade": student.previousGrade,
        "extracurricularActivities": student.extracurricularActivities,
        "parentalSupport": student.parentalSupport,
        "finalGrade": student.finalGrade,
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
            "attendanceRate": student.attendanceRate,
            "studyHoursPerWeek": student.studyHoursPerWeek,
            "previousGrade": student.previousGrade,
            "extracurricularActivities": student.extracurricularActivities,
            "parentalSupport": student.parentalSupport,
            "finalGrade": student.finalGrade,
        })

        return {"students": result}
