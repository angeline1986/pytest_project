@login
Feature: Confirm full order preparation
  As a user of Supplier Portal
  The user would like to Reject an order
  To inform the customers/BEES that the order will be fulfilled

#  Background:
#    Given The user is logged in to the Supplier Portal


  Scenario: User confirm a full order preparation
    Given the user access the Order Management Page
    And the user access the To be prepared sub-tab
    When the user clicks on the first order