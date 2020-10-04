# Created by sona at 10/3/2020
Feature: Test for amazon Help search
  # Enter feature description here

  Scenario: Amazon help search lets to search for help
   Given Open Amazon help page
    When Input cancel order into help search field
    Then Press Enter on help Search icon
    Then Search result Cancel Items or Orders  is shown