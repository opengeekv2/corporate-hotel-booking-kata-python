from enum import Enum
from typing import List


class RoomType(Enum):
    SINGLE_ROOM = 1


class Room:
    number: int
    type: RoomType

    def __init__(self, number: int, type: RoomType):
        self.number = number
        self.type = type


class Hotel:
    id: int
    name: str
    rooms: List[Room]

    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name
        self.rooms = []

    def add_room(self, room: Room):
        self.rooms.insert(room.number, room)
