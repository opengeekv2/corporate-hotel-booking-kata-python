from unittest import mock
from corporate_hotel_booking_kata_python.domain.hotel_service import add_hotel
from corporate_hotel_booking_kata_python.domain.model import Hotel


@mock.patch("corporate_hotel_booking_kata_python.domain.hotel_service.save")
def test_hotel_service_add_hotel(hotel_repository_save: mock.MagicMock):
    add_hotel(0, "Faulty Towers")
    hotel: Hotel = hotel_repository_save.call_args.args[0]
    assert hotel.id == 0
    assert hotel.name == "Faulty Towers"
