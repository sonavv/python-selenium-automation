# Created by sona at 10/17/2020
Feature: Verify adding item is successful
  # Enter feature description here

  Scenario: When user adds an item to the cart, it should reflect in the cart

    Given Open Amazon frontpage
    When Input vase into amazon search
    Then Click on the search icon
    Then Add the first item to the cart
    Then click on the add icon
    Then verify the cart has the item