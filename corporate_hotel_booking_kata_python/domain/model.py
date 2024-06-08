from datetime import date
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
    employee_id: int
    hotel_id: int
    room_type: str
    checkin_date: date
    checkout_date: date

    def __init__(self, id: UUID, employee_id: int, hotel_id: int, room_type: str, checkin_date: date, checkout_date: date):
        self.id = id
        self.employee_id = employee_id
        self.hotel_id = hotel_id
        self.room_type = room_type
        self.checkin_date = checkin_date
        self.checkout_date = checkout_date


