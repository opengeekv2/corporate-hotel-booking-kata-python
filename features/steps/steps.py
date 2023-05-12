from unittest import mock
from behave import given, when, then
from corporate_hotel_booking_kata_python.domain import hotel_service
from fake_infrastructure.hotel_repository import get, save


@given(u'a hotel management system')
def step_impl(context):
    pass

@when(u'we create a new hotel')
@mock.patch("corporate_hotel_booking_kata_python.domain.hotel_service.save", new=save)
def step_impl(context):
    hotel_service.add_hotel(0, "Fawlty Towers")

@when(u'a room')
@mock.patch("corporate_hotel_booking_kata_python.domain.hotel_service.save", new=save)
@mock.patch("corporate_hotel_booking_kata_python.domain.hotel_service.get", new=get)
def step_impl(context):
    hotel_service.set_room(0, 0, hotel_service.RoomType.SINGLE_ROOM)


@when(u'another room')
def step_impl(context):
    raise NotImplementedError(u'STEP: When another room')


@then(u'the hotel has two rooms')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the hotel has two rooms')