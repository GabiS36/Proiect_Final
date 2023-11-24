Feature: Ebay cart with products feature

  Background:
    Given Cart: the user is on the cart page with products added

  @test1
  Scenario:  Test Subtotal is correct
  Then Cart: I check that the subtotal is correct US $0.99

  @test2
  Scenario: Test cart icon count is correct
  Then Cart: I check that the cart icon in the header displays the correct number of products: 1

  @test3
  Scenario: Test cart remove product functionality
  When Cart: I click the Remove link
  Then Cart: I check the empty cart message


