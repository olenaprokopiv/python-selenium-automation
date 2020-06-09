# Created by lena at 6/8/2020
Feature: Scenarios for Cart functionality

  Scenario: User can verify Amazon Cart is empty
    Given Open Amazon page
    When Click cart button
    Then Verify text Your Amazon Cart is empty on the cart page