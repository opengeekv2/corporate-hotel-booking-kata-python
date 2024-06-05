from corporate_hotel_booking_kata_python.domain.model import Company, Employee
from corporate_hotel_booking_kata_python.domain.ports import company_repository


def add_employee(companyId: int, employeeId: int):
    company: Company = company_repository.get(companyId)
    if company is None:
        company = Company(0)
    company.employees.insert(employeeId, Employee(employeeId))
    company_repository.save(company)