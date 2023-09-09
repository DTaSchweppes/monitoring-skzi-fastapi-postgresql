from sqlalchemy import Column, String, Integer

from config import Base


class Employee(Base):
    __tablename__ = 'employeers'

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    pos = Column(String)
    department = Column(String)
    contact_number = Column(String)
    table_number = Column(String)
