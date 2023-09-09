from pydantic import BaseModel, Field


class EmployeeBase(BaseModel):
    first_name: str = Field(..., max_length=50)
    last_name: str = Field(..., max_length=50)
    pos: str = Field(..., max_length=100)
    department: str = Field(..., max_length=100)
    contact_number: str = Field(..., max_length=15)
    table_number: str = Field(..., max_length=10)


class EmployeeCreate(EmployeeBase):
    pass


class EmployeeUpdate(EmployeeBase):
    pass


class Employee(EmployeeBase):
    id: int

    class Config:
        orm_mode = True