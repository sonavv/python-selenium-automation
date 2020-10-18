# Created by sona at 10/17/2020
Feature: Verify Amazon Cart empty


  Scenario: Verify cart is empty
   Given Open Amazon Homepage
    When click the cart icon
    Then Verify the page shows Your Amazon Cart is empty
