from datetime import date
from pydantic import BaseModel
from enum import StrEnum, auto
from datetime import datetime

from hotel.db.db_interface import DataObject
from hotel.operations.interface import DataInterface

class RoomCreateData(BaseModel):  # type: ignore
    room_id: int
    number: int
    size: int
    price: int

class BookingUpdateData(BaseModel):  # type: ignore
    room_id = int
    number: int
    size: int
    price: int

class RoomStatus(StrEnum):
    AVAILABLE = auto()
    BOOKED = auto()

ROOM_STATUS: dict[RoomStatus, str] = {
    RoomStatus.AVAILABLE: "AVAILABLE",
    RoomStatus.BOOKED: "BOOKED",
}

def read_all_rooms(room_interface: DataInterface) -> list[DataObject]:
    return room_interface.read_all()


def read_room(room_id: int, room_interface: DataInterface):
    return room_interface.read_by_id(room_id)

def create_room(
        data: RoomCreateData,
        room_interface: DataInterface
) -> DataObject:
    room_dict = data.dict()  # type: ignore

    return room_interface.create(room_dict)  # type: ignore


def delete_room(room_id: int, room_interface: DataInterface) -> DataObject:
    return room_interface.delete(room_id) 


def check_room_status(
        room_id: int,
        date: date, 
        booking_interface: DataInterface
) -> str:
    
    bookings: list[DataObject] = booking_interface.read_all()

    for booking in bookings:
        if booking["room_id"] == room_id and booking["from_date"] == date:  # type: ignore
            return ROOM_STATUS[RoomStatus.BOOKED]

    return ROOM_STATUS[RoomStatus.AVAILABLE]


def get_rooms_available_between(from_date: date, to_date: date, booking_interface: DataInterface) -> list[int]:
    bookings: list[DataObject] = booking_interface.read_all()

    datetime_format = "%Y-%m-%d"
    begin_date: date = datetime.strptime(from_date, datetime_format)  # type: ignore
    end_date: date = datetime.strptime(to_date, datetime_format)  # type: ignore
    
    available_rooms: list[int] = []
    for booking in bookings:
        booking_from_date = datetime.strptime(booking["from_date"], datetime_format)
        booking_to_date = datetime.strptime(booking["to_date"], datetime_format)
        """ # Neither begin nor end dates must lie between from_date and to_date of any particular booking
        is_begin_date_in_between: bool = booking_from_date < begin_date < booking_to_date  # type: ignore 
        is_end_date_in_between: bool = booking_from_date < end_date < booking_to_date  # type: ignore
        if not is_begin_date_in_between and not is_end_date_in_between: """
        if begin_date > booking_to_date or end_date < booking_from_date:
            available_rooms.append(booking["room_id"])  

    return list(set(available_rooms))
