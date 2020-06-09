# Created by lena at 6/8/2020
Feature: Scenarios for Help functionality

  Scenario: User can search for Cancelling an order
    Given Open Amazon Help page
    When Search for Cancel order
    And Click submit button
    Then Verify text Cancel Items or Orders is shown