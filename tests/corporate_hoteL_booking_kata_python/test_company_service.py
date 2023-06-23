from unittest import mock

from corporate_hotel_booking_kata_python.domain.company_service import add_employee
from corporate_hotel_booking_kata_python.domain.model import Company


@mock.patch("corporate_hotel_booking_kata_python.domain.company_service.save")
def test_company_service_add_employee(company_repository_save: mock.MagicMock):
    add_employee(0, 0)
    company: Company = company_repository_save.call_args.args[0]
    assert 0 in [employee.id for employee in company.employees]
