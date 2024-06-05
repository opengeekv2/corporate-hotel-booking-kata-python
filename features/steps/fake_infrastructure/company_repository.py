from corporate_hotel_booking_kata_python.domain.model import Company

_companies = []
def save(company: Company):
    _companies.insert(company.id, company)

def get(id: int) -> Company:
    return _companies[id]