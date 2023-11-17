Feature: Ebay products feature

  Background:
    Given Products: the user is on the product details page

  @test10
  Scenario: Test Add product to cart functionality
  When Products: the user clicks on the "Add to Cart" button
  Then Cart: the selected product should be added to the shopping cart
