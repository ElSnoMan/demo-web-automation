Feature: Add two numbers and return the sum

  Scenario: Adding two even numbers returns an even number
    Given x=2 and y=2
    When I add them together
    Then the sum should be 4
    And be even

  Scenario: Adding two negative numbers returns a negative number
    Given x=-2
    And y=-2
    When I add them together
    Then the sum should be -4
    And be negative

  Scenario: Create your own
    Given
    When
    Then
