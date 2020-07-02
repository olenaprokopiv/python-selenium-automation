# Created by lena at 6/30/2020
Feature:  User can open and close Amazon Blog

  Scenario:  User can open and close Amazon Blog
    Given Open Amazon page
    When Click on blog link “See daily updates at blog.aboutamazon.com”
    And Switch to the new opened window
    Then Amazon Blog daily updates is opened
    And User can close new window and switch back to original
