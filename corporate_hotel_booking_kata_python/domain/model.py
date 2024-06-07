from enum import Enum, StrEnum, auto
from typing import List
from uuid import UUID


class RoomType(StrEnum):
    SINGLE_ROOM = auto()


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


class Employee:
    id: int

    def __init__(self, id: int):
        self.id = id



class Company:
    id: int
    employees: List[Employee]

    def __init__(self, id: int):
        self.id = id
        self.employees = []

class Booking:
    id: UUID

    def __init__(self, id: UUID):
        self.id = id

