# Created by sona at 9/30/2020
Feature: Tests for Amazon Search
  # Enter feature description here

  Scenario: Amazon search returns correct result
    Given Open Amazon page
    When Input Dress into Amazon search field
    And Click on Amazon Search icon
    Then Search result Dress is shown


    Scenario: Amazon users see sign up button
      Given Open Amazon page
      Then Verify Sign In is Clickable
      When Wait for 9 sec
      Then Verify Sign In is clickable
      Then Verify Sign In disappears
