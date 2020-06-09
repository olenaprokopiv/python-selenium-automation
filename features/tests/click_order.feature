# Created by lena at 6/8/2020
Feature: Test for Main page

  Scenario: Logged out user sees Sign in page when clicking Orders
    Given Open Amazon page
    When Click Orders
    Then Verify Sign in page opened
    And Verify URL has https://www.amazon.com/ap/signin