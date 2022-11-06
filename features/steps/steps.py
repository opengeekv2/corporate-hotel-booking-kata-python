from behave import given, when, then
from corporate_hotel_booking_kata_python.domain import hotel_service


@given(u'a hotel management system')
def step_impl(context):
    pass

@when(u'we create a new hotel')
def step_impl(context):
    hotel_service.add_hotel(0, "Fawlty Towers")

@when(u'a room')
def step_impl(context):
    raise NotImplementedError(u'STEP: When a room')


@when(u'another room')
def step_impl(context):
    raise NotImplementedError(u'STEP: When another room')


@then(u'the hotel has two rooms')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the hotel has two rooms')