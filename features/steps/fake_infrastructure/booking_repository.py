from typing import Optional
from uuid import UUID

from corporate_hotel_booking_kata_python.domain.model import Company, Booking

_bookings = {}
def save(booking: Booking) -> Booking:
    _bookings[str(booking.id)] = booking
    return booking

def get(id: UUID) -> Optional[Company]:
    try:
        return _bookings[str(id)]
    except IndexError:
        return None

