Feature: Manage hotels

  Scenario: Create hotel and some rooms for it
      Given a hotel management system
       When we create a new hotel
       And a room
       And another room
       Then the hotel has two rooms