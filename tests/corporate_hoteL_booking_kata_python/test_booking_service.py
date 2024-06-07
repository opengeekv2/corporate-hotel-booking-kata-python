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
    booking_repository.save = MagicMock(return_value=Booking(uuid.UUID(booking_uuid)))
    guid_generator.get = MagicMock(return_value=uuid.UUID(booking_uuid))
    booking = booking_service.book_room(0, 0, 'SINGLE_ROOM', datetime.date(2024,2,14), datetime.date(2024,2,14))
    assert str(booking_repository.save.call_args_list[0][0][0].id) == booking_uuid
    assert str(booking.id) == booking_uuid


