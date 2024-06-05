from unittest import mock
from unittest.mock import MagicMock

from corporate_hotel_booking_kata_python.domain import booking_service
from corporate_hotel_booking_kata_python.domain.company_service import add_employee
from corporate_hotel_booking_kata_python.domain.model import Company


@mock.patch("corporate_hotel_booking_kata_python.domain.booking_service.booking_repository")
def test_book_without_issues(booking_repository: MagicMock):
    booking_repository.save = MagicMock()
    booking = booking_service.book_room()
    assert booking is not None

