# Created by sona at 10/27/2020
Feature: Amazon main page


  Scenario: Sign_In popup disappears
    Given Open Amazon
    Then Sign-In popup is present and clickable
    When Sign_In popup disappears
    Then Verify Sign-In popup is not clickable

