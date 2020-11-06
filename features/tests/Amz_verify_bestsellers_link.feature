# Created by sona at 10/18/2020
Feature: Verify there are five links under best sellers
  # Enter feature description here

  Scenario: Verify links under best sellers
    Given Open the Best Sellers page in Amazon
    Then Verify there are 5 links

  Scenario: Links on the Bestseller page works
    Given Open the Best Sellers page in Amazon
    Then User can click all the links on the top and verify it opens the correct page
