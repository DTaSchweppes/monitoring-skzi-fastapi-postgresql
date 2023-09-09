from pydantic import BaseModel

class EmployeeShiftBase(BaseModel):
    employee_id: int
    shift_id: int


class EmployeeShiftCreate(EmployeeShiftBase):
    pass


class EmployeeShift(EmployeeShiftBase):
    id: int

    class Config:
        orm_mode = True