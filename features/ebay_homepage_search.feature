Feature: Ebay search functionality

  Background:
    Given Home page: I am a user on ebay home page

  @test4 @test5
  Scenario Outline: Test simple search functionality
    When Home page: I search for "<query>" from category "<category_name>"
    Then Home page: I have at least "<no_of_results>" results returned

    Examples:
    |query       |category_name              |no_of_results|
    |iphone      |Cell Phones & Accessories  |1000         |
    |TV          |Consumer Electronics       |10000        |

  @test6
  Scenario Outline: Test advanced search functionality
    When Home page: I click on the advanced link
    When Advanced search page: I type "<search_term>" in the enter keyword textbox
    When Advanced search page: I select a keyword option from keyword options
    When Advanced search page: I choose "<category>" from the category list
    When Advanced search page: I click search button
    Then Home page: I have at least "<no_of_results>" results returned
    Examples:
      |search_term |category                      |no_of_results |
      |Pampers     |Baby                          |1000          |
      |Toys        |Dolls & Bears                 |100000        |
      |Canon       |Cameras & Photo               |10000         |
      |Apple       |Computers/Tablets & Networking|1000          |

  @test7
  Scenario: Test access product from the product results page
    When Home page: the user is on the product results page
    When Home page: the user selects a product and a new tab opens
    Then Products: the user should see detailed information about the selected product