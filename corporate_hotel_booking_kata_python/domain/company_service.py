from corporate_hotel_booking_kata_python.domain.model import Company, Employee
from corporate_hotel_booking_kata_python.domain.ports import company_repository


def add_employee(company_id: int, employee_id: int):
    company: Company = company_repository.get(company_id)
    if company is None:
        company = Company(company_id)
    company.employees.insert(employee_id, Employee(employee_id))
    company_repository.save(company)