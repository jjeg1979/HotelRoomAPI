from datetime import date
from fastapi import APIRouter
from hotel.db.db_interface import DBInterface, DataObject
from hotel.db.models import DBBooking, DBRoom

from hotel.operations.rooms import (
    RoomCreateData, 
    read_all_rooms, 
    read_room, 
    create_room,
    check_room_status,
    get_rooms_available_between,
)

router = APIRouter()  # type: ignore


@router.get("/rooms")  # type: ignore
def api_red_all_rooms() -> list[DataObject]:
    room_interface = DBInterface(DBRoom)
    return read_all_rooms(room_interface)

@router.get("/room/{room_id}")  # type: ignore
def api_read_room(room_id: int) -> DataObject:
    room_interface = DBInterface(DBRoom)
    return read_room(room_id, room_interface)

@router.post("/room")  # type: ignore
def api_create_room(room: RoomCreateData) -> DataObject:
    room_interface = DBInterface(DBRoom)
    return create_room(room, room_interface)

@router.get("/room/status/{room_id}/{tentative_date}")  # type: ignore
def api_check_room_status(room_id: int, tentative_date: date) -> str:    
    booking_interface = DBInterface(DBBooking)
    return check_room_status(room_id, tentative_date, booking_interface)

@router.get("/rooms/available/{from_date}_{to_date}")  # type: ignore
def api_check_rooms_available_between(from_date: date, to_date: date) -> list[int]:
    booking_interface = DBInterface(DBBooking)
    return get_rooms_available_between(from_date, to_date, booking_interface)
