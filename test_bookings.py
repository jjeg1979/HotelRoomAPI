import unittest

from hotel.db.db_interface import DataObject

from hotel.operations.bookings import InvalidDateError, BookingCreateData, create_booking
from hotel.operations.rooms import check_room_status, get_rooms_available_between


class DataInterfaceStub:
    def read_by_id(self, id: int) -> DataObject:
        raise NotImplementedError()

    def read_all(self) -> list[DataObject]:
        raise NotImplementedError()

    def create(self, data: DataObject) -> DataObject:
        raise NotImplementedError()

    def update(self, id: int, data: DataObject) -> DataObject:
        raise NotImplementedError()

    def delete(self, id: int) -> DataObject:
        raise NotImplementedError()


class RoomInterface(DataInterfaceStub):
    def read_by_id(self, id: int) -> DataObject:
        return {"id": id, "number": "101", "size": 10, "price": 150_00}


class BookingInterface(DataInterfaceStub):
    def create(self, data: DataObject) -> DataObject:
        booking = dict(data)
        booking["id"] = 1
        return booking
    
    def read_all(self) -> list[DataObject]:
        bookings = [
            {"room_id": 1, "customer_id": 1, "from_date": "2023-06-01", "to_date": "2023-06-15"},
            {"room_id": 1, "customer_id": 2, "from_date": "2023-06-15", "to_date": "2023-06-30"},
            {"room_id": 2, "customer_id": 3, "from_date": "2021-01-01", "to_date": "2021-01-10"},
        ]
        return bookings


class TestBooking(unittest.TestCase):
    def test_price_one_day(self):
        booking_data = BookingCreateData(
            room_id=1, customer_id=1, from_date="2021-12-24", to_date="2021-12-25"  # type: ignore
        )
        booking = create_booking(data=booking_data,                                 
                                 booking_interface=BookingInterface(),
                                 room_interface=RoomInterface())
        self.assertEqual(booking["price"], 150_00)

    def test_date_error(self):
        booking_data = BookingCreateData(
            room_id=1, customer_id=1, from_date="2021-12-24", to_date="2021-12-24"  # type: ignore
        )

        self.assertRaises(InvalidDateError, create_booking, booking_data, BookingInterface(), RoomInterface())

    def test_room_status_is_available(self):
        room_id = 1
        desired_date = "2023-01-01"        
        status = check_room_status(room_id, desired_date, BookingInterface())  # type: ignore
        self.assertEqual(status, "AVAILABLE")

    def test_room_status_is_booked(self):
        room_id = 1
        desired_date = "2023-06-01"        
        status = check_room_status(room_id, desired_date, BookingInterface())  # type: ignore
        self.assertEqual(status, "BOOKED")

    def test_get_rooms_available_between_dates(self):        
        rooms = get_rooms_available_between("2021-01-01", "2021-06-01", BookingInterface())  # type: ignore
        self.assertListEqual(rooms, [1])

if __name__ == "__main__":
    unittest.main()
