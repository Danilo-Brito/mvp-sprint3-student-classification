from sqlalchemy import Column, String, Integer, DateTime, Float
from datetime import datetime
from typing import Union
from model import Base


#  StudentID,
#  Name,
#  Gender,
#  AttendanceRate,
#  StudyHoursPerWeek,
#  PreviousGrade,
#  ExtracurricularActivities,
#  ParentalSupport,
#  FinalGrade

class Student(Base):
    __tablename__ = 'student'

    id = Column(Integer, primary_key=True)
    name = Column("Name", String(50))
    gender = Column("Gender", String(50))
    attendanceRate = Column("AttendanceRate", Integer)
    studyHoursPerWeek = Column("StudyHoursPerWeek", Integer)
    previousGrade = Column("PreviousGrade", Integer)
    extracurricularActivities = Column("ExtracurricularActivities", Integer)
    parentalSupport = Column("ParentalSupport", String(50))
    finalGrade = Column("FinalGrade", Integer, nullable=True)
    data_insert = Column(DateTime, default=datetime.now())


def __init__(self, name: str, gender: int, attendanceRate: int,
             studyHoursPerWeek: int, previousGrade: int, extracurricularActivities: int,
             parentalSupport: str, finalGrade: int,
             data_insert: Union[DateTime, None] = None):
    self.name = name
    self.gender = gender
    self.attendanceRate = attendanceRate
    self.studyHoursPerWeek = studyHoursPerWeek
    self.previousGrade = previousGrade
    self.extracurricularActivities = extracurricularActivities
    self.parentalSupport = parentalSupport
    self.finalGrade = finalGrade

    if data_insert:
        self.data_insert = data_insert
