# Created by sona at 11/19/2020
Feature:
  # Enter feature description here

  Scenario: Amazon Music has 7 menu items
    Given Open Amazon Page to Find Hamburger Icon
    When Click hamburger menu icon
    Then Click Amazon Music from the menu
    Then Verify there are 7 items in the menu