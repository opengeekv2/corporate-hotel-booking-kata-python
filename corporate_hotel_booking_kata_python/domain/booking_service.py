from datetime import date

from corporate_hotel_booking_kata_python.domain.model import Booking
from corporate_hotel_booking_kata_python.domain.ports import booking_repository, guid_generator


def book_room(employee_id: int, hotel_id: int, room_type: str, checkin_date: date, checkout_date: date):
    return booking_repository.save(Booking(guid_generator.get(), employee_id, hotel_id, room_type, checkin_date, checkout_date))