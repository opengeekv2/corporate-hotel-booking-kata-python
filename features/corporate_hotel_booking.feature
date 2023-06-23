Feature: Manage hotels

  Scenario: Employee can book a room
    Given a hotel management system
     And we create a new hotel
     And a room
     And an employee
    When employee books a room
    Then he can book a room
