from datetime import date
from typing import Optional

from hotel.operations.interface import DataObject, DataInterface
from pydantic import BaseModel


class InvalidDateError(Exception):
    pass


class BookingCreateData(BaseModel):  # type: ignore
    room_id: int
    customer_id: int
    from_date: date
    to_date: date


class BookingUpdateData(BaseModel):  # type: ignore
    room_id: Optional[int]
    customer_id: Optional[int]
    from_date: Optional[date]
    to_date: Optional[date]


def read_all_bookings(booking_interface: DataInterface) -> list[DataObject]:
    return booking_interface.read_all()


def read_booking(
        booking_id: int,
        booking_interface: DataInterface
) -> DataObject:
    return booking_interface.read_by_id(booking_id)


def create_booking(
    data: BookingCreateData,
    booking_interface: DataInterface,
    room_interface: DataInterface,
) -> DataObject:
    
    # retrieve the room
    room = room_interface.read_by_id(data.room_id)

    days = (data.to_date - data.from_date).days
    if days <= 0:
        raise InvalidDateError("Invalid dates.")

    booking_dict = data.dict()  # type: ignore
    booking_dict["price"] = room["price"] * days

    return booking_interface.create(booking_dict)  # type: ignore


def update_booking(
        booking_id: int,
        data: BookingUpdateData,
        booking_interface: DataInterface
) -> DataObject:
    return booking_interface.update(booking_id, data)  # type: ignore


def delete_booking(
    booking_id: int,
    booking_interface: DataInterface,
) -> DataObject:
    return booking_interface.delete(booking_id)
