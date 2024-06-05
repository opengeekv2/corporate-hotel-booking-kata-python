from unittest import mock
from unittest.mock import MagicMock

from corporate_hotel_booking_kata_python.domain.company_service import add_employee
from corporate_hotel_booking_kata_python.domain.model import Company


@mock.patch("corporate_hotel_booking_kata_python.domain.company_service.company_repository")
def test_add_employee(company_repository: MagicMock):
    company_repository.get = MagicMock(return_value=Company(0))
    company_repository.save = MagicMock()
    add_employee(0, 0)
    company: Company = company_repository.save.call_args.args[0]
    assert company.id == 0
    assert 0 in [employee.id for employee in company.employees]

@mock.patch("corporate_hotel_booking_kata_python.domain.company_service.company_repository")
def test_add_employee_and_company_when_not_existing(company_repository: MagicMock):
    company_repository.get = MagicMock(return_value=None)
    company_repository.save = MagicMock()
    add_employee(0, 0)
    company: Company = company_repository.save.call_args.args[0]
    assert company.id == 0
    assert 0 in [employee.id for employee in company.employees]
