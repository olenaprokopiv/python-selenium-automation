# Created by lena at 6/26/2020
Feature: Verify every product on the page has a text 'Regular' and a product name

  Scenario: Verify every product on the page has a text 'Regular' and a product name
    Given Open Amazon wholefoodsdesls page
    Then Verify all product has text Regular field and name
