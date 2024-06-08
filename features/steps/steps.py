import datetime
from unittest import mock
from unittest.mock import MagicMock
from uuid import UUID

from behave import given, when, then
from corporate_hotel_booking_kata_python.domain import hotel_service, company_service, booking_service
from fake_infrastructure.hotel_repository import get, save
from features.steps.fake_infrastructure import company_repository, booking_repository

_booking = None

@given(u'a hotel management system')
def step_impl(context):
    pass

@given(u'we create a new hotel')
@mock.patch("corporate_hotel_booking_kata_python.domain.hotel_service.save", new=save)
def step_impl(context):
    hotel_service.add_hotel(0, "Fawlty Towers")

@given(u'a room')
@mock.patch("corporate_hotel_booking_kata_python.domain.hotel_service.save", new=save)
@mock.patch("corporate_hotel_booking_kata_python.domain.hotel_service.get", new=get)
def step_impl(context):
    hotel_service.set_room(0, 0, hotel_service.RoomType.SINGLE_ROOM)

@given(u'an employee')
@mock.patch("corporate_hotel_booking_kata_python.domain.company_service.company_repository", new=company_repository)
def step_impl(context):
    company_service.add_employee(0, 0)

guid_generator = MagicMock()
guid_generator.get = MagicMock(return_value=UUID("84ab1798-4f0f-4a96-a151-6735ca9bc969"))


@when(u'employee books a room')
@mock.patch("corporate_hotel_booking_kata_python.domain.booking_service.booking_repository", new=booking_repository)
@mock.patch("corporate_hotel_booking_kata_python.domain.booking_service.guid_generator", new=guid_generator)
def step_impl(context):
    context.booking = booking_service.book_room(
        0,
        0,
        'SINGLE_ROOM',
        datetime.date(2024, 2, 14),
        datetime.date(2024, 3, 14)
    )

@then(u'he can book a room')
def step_impl(context):
    assert context.booking is not None

