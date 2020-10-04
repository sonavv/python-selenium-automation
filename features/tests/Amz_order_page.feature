# Created by sathi at 10/3/2020
Feature: Test the order page
  # Enter feature description here

  Scenario: Order click has to open sign in page
    Given Open Amazon home page
    When click the order button
    Then sign in page has to open