from sqlalchemy import Column, String, Integer, DateTime, Float
from datetime import datetime
from typing import Union
from model import Base


class Student(Base):
    __tablename__ = 'student'

    id = Column(Integer, primary_key=True)
    name = Column("Name", String(50))
    gender = Column("Gender", Integer)
    attendance_rate = Column("AttendanceRate", Integer)
    study_hours_per_week = Column("StudyHoursPerWeek", Integer)
    previous_grade = Column("PreviousGrade", Integer)
    extracurricular_activities = Column("ExtracurricularActivities", Integer)
    parental_support = Column("ParentalSupport", Integer)
    final_grade = Column("FinalGrade", Integer, nullable=True)
    data_insert = Column(DateTime, default=datetime.now())


def __init__(self, name: str, gender: int, attendance_rate: int,
             study_hours_per_week: int, previous_grade: int, extracurricular_activities: int,
             parental_support: int, final_grade: int,
             data_insert: Union[DateTime, None] = None):
    self.name = name
    self.gender = gender
    self.attendance_rate = attendance_rate
    self.study_hours_per_week = study_hours_per_week
    self.previous_grade = previous_grade
    self.extracurricular_activities = extracurricular_activities
    self.parental_support = parental_support
    self.final_grade = final_grade

    if data_insert:
        self.data_insert = data_insert
