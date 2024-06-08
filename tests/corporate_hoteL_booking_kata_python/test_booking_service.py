import datetime
import uuid
from unittest import mock
from unittest.mock import MagicMock


from corporate_hotel_booking_kata_python.domain import booking_service
from corporate_hotel_booking_kata_python.domain.model import Booking


@mock.patch("corporate_hotel_booking_kata_python.domain.booking_service.booking_repository")
@mock.patch("corporate_hotel_booking_kata_python.domain.booking_service.guid_generator")
def test_book_without_issues(guid_generator: MagicMock, booking_repository: MagicMock):
    booking_uuid = "84ab1798-4f0f-4a96-a151-6735ca9bc969"
    employee_id = 0
    hotel_id = 0
    room_type = 'SINGLE_ROOM'
    checkin_date = datetime.date(2024, 2, 14)
    checkout_date = datetime.date(2024, 2, 15)

    booking_repository.save = MagicMock(return_value=Booking(uuid.UUID(booking_uuid), employee_id, hotel_id, room_type, checkin_date, checkout_date))
    guid_generator.get = MagicMock(return_value=uuid.UUID(booking_uuid))
    booking = booking_service.book_room(employee_id, hotel_id, room_type, checkin_date, checkout_date)

    assert str(booking_repository.save.call_args_list[0][0][0].id) == booking_uuid
    assert booking_repository.save.call_args_list[0][0][0].employee_id == employee_id
    assert booking_repository.save.call_args_list[0][0][0].hotel_id == hotel_id
    assert booking_repository.save.call_args_list[0][0][0].room_type == room_type
    assert booking_repository.save.call_args_list[0][0][0].checkin_date == checkin_date
    assert booking_repository.save.call_args_list[0][0][0].checkout_date == checkout_date



    assert str(booking.id) == booking_uuid
    assert booking.employee_id == employee_id
    assert booking.hotel_id == hotel_id
    assert booking.room_type == room_type
    assert booking.checkin_date == checkin_date
    assert booking.checkout_date == checkout_date





