Feature: Add to Cart

  Background:
    Given Products: the user is on the product details page

  Scenario: Add product to cart
    When Products: the user clicks on the "Add to Cart" button
    Then Cart: the selected product should be added to the shopping cart