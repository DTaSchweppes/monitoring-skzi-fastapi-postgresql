from fastapi import APIRouter
from models.shift import Shift
from api.schemas.shift import ShiftCreate
from api.db import db_session

router = APIRouter()

@router.post("/shifts")
async def create_shift(shift: ShiftCreate):
    shift_data = shift.dict()
    db_shift = Shift(**shift_data)

    db_session.add(db_shift)
    await db_session.flush()  # Фиксируем изменения в сессии

    try:
        await db_session.commit()  # Сохраняем изменения в базе данных
        return {"message": "Shift created successfully"}
    except Exception as e:
        await db_session.rollback()  # Откатываем изменения в случае ошибки
        return {"message": f"Failed to create shift. Error: {str(e)}"}
    finally:
        await db_session.close()  # Закрываем сессию базы данных