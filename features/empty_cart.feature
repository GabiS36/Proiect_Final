Feature: Ebay empty cart feature

  Background:
    Given Home page: I am a user on ebay home page

  @test8
  Scenario: Test the empty cart icon dialog
    When Home page: I hover the cart icon in the header
    Then Home page: I verify empty cart icon dialog title


 @test9
 Scenario: Test clicking the cart icon in the header redirects the user to the cart page
   When Home page: I click the cart icon in the header
   Then Cart: I verify the cart page URL is correct



