from pydantic import BaseModel
from datetime import datetime


class ShiftBase(BaseModel):
    shift_start_time: datetime
    shift_end_time: datetime


class ShiftCreate(ShiftBase):
    pass


class Shift(ShiftBase):
    id: int

    class Config:
        orm_mode = True