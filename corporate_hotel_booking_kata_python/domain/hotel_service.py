from enum import Enum

from corporate_hotel_booking_kata_python.domain.ports.hotel_repository import get, save
from corporate_hotel_booking_kata_python.domain.model import Hotel, RoomType, Room


def add_hotel(id: int, name: str) -> None:
    save(Hotel(id, name))


def set_room(hotel_id: int, room: int, room_type: RoomType):
    hotel = get(hotel_id)
    hotel.add_room(Room(room, room_type))
    save(hotel)
