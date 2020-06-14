# Created by lena at 6/14/2020
Feature: Test case for amazon BestSellers page

  Scenario: Verify there are 5 links in BestSellers page
    Given Open Amazon page
    When Click BestSellers button
    Then Click on each tab and verify correct page opens

