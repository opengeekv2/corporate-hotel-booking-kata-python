from unittest import mock
from corporate_hotel_booking_kata_python.domain.hotel_service import add_hotel, set_room, RoomType
from corporate_hotel_booking_kata_python.domain.model import Hotel


@mock.patch("corporate_hotel_booking_kata_python.domain.hotel_service.save")
def test_hotel_service_add_hotel(hotel_repository_save: mock.MagicMock):
    add_hotel(0, "Faulty Towers")
    hotel: Hotel = hotel_repository_save.call_args.args[0]
    assert hotel.id == 0
    assert hotel.name == "Faulty Towers"


@mock.patch("corporate_hotel_booking_kata_python.domain.hotel_service.get")
@mock.patch("corporate_hotel_booking_kata_python.domain.hotel_service.save")
def test_hotel_service_set_room(hotel_repository_save: mock.MagicMock, hotel_repository_get: mock.MagicMock):
    hotel_repository_get.return_value = Hotel(0, "Faulty Towers")
    set_room(0, 0, RoomType.SINGLE_ROOM)
    hotel: Hotel = hotel_repository_save.call_args.args[0]
    assert hotel.rooms[0].number == 0
    assert hotel.rooms[0].type == RoomType.SINGLE_ROOM
