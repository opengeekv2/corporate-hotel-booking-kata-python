from corporate_hotel_booking_kata_python.domain.ports.hotel_repository import save
from corporate_hotel_booking_kata_python.domain.model import Hotel

def add_hotel(id: int, name: str) -> None:
    save(Hotel(id, name))