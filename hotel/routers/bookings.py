from fastapi import APIRouter
from hotel.db.db_interface import DBInterface, DataObject
from hotel.db.models import DBBooking, DBRoom

from hotel.operations.bookings import (
    BookingUpdateData,
    BookingCreateData,
    read_all_bookings,
    read_booking,
    create_booking,
    delete_booking,
    update_booking,
)


router = APIRouter()  # type: ignore


@router.get("/bookings")  # type: ignore
def api_red_all_bookings() -> list[DataObject]:
    booking_interface = DBInterface(DBBooking)
    return read_all_bookings(booking_interface)


@router.get("/booking/{booking_id}")  # type: ignore
def api_read_booking(booking_id: int) ->DataObject:
    booking_interface = DBInterface(DBBooking)
    return read_booking(booking_id, booking_interface)


@router.post("/booking")  # type: ignore
def api_create_booking(booking: BookingCreateData) -> DataObject:
    booking_interface = DBInterface(DBBooking)
    room_interface = DBInterface(DBRoom)
    return create_booking(booking, booking_interface, room_interface)


@router.post("/booking/{booking_id}")  # type: ignore
def api_update_booking(booking_id: int, booking: BookingUpdateData) -> DataObject:
    booking_interface = DBInterface(DBBooking)
    return update_booking(booking_id, booking, booking_interface)


@router.delete("/booking/{booking_id}")  # type: ignore
def api_delete_booking(booking_id: int) -> DataObject:
    booking_interface = DBInterface(DBBooking)
    return delete_booking(booking_id, booking_interface)
