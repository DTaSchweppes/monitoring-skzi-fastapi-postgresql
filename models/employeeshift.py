from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from config import Base

class EmployeeShift(Base):
    __tablename__ = 'employee_shifts'

    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(Integer, ForeignKey('employees.id'))
    shift_id = Column(Integer, ForeignKey('shifts.id'))

    employee = relationship("Employee", back_populates="shifts")
    shift = relationship("Shift", back_populates="employees")