from corporate_hotel_booking_kata_python.domain.model import Hotel

_hotels = []
def save(hotel: Hotel):
    _hotels.insert(hotel.id, hotel)

def get(id: int) -> Hotel:
    return _hotels[id]