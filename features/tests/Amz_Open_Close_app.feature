# Created by sona at 10/29/2020
Feature: Verify new window is opened
  # Enter feature description here

  Scenario: User can open and close Amazon Applications

 Given Open Amazon T&C page
 Then Click on Amazon applications link
 When Switch to the newly opened window
 Then Amazon app page is opened
 Then User can close new window and switch back to original
