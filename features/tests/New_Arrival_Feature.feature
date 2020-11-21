# Created by sona at 11/20/2020
Feature: Tests for New Arrivals Feature
  # Enter feature description here

  Scenario: When the User hovers on New Arrivals corresponding deals are shown

    Given Open Amazon product page
    When Hover over New Arrivals tab
    Then Verify the deals are shown