import datetime
from unittest import mock
from behave import given, when, then
from corporate_hotel_booking_kata_python.domain import hotel_service, company_service, booking_service
from fake_infrastructure.hotel_repository import get, save
from features.steps.fake_infrastructure import company_repository


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

@when(u'employee books a room')
def step_impl(context):
    booking_service.book_room(
        0,
        0,
        'SINGLE_ROOM',
        datetime.date(2024, 2, 14),
        datetime.date(2024, 3, 14)
    )

