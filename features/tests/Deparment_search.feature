# Created by Sona at 11/20/2020
Feature: User can Select and Search in a department
  # User can select a particular department from the dropdown menu and search an item in it.

  Scenario: User can search and select a department
    Given Open Amazon main page
    When select Appliances department
    Then Search for Kettle
    Then Verify Appliances department is selected