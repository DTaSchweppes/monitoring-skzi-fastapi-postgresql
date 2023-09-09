from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.orm import relationship

from config import Base


class Shift(Base):
    __tablename__ = 'shifts'

    id = Column(Integer, primary_key=True, index=True)
    shift_start_time = Column(DateTime)
    shift_end_time = Column(DateTime)

    employees = relationship("Employee", secondary="employee_shifts", back_populates="shifts")