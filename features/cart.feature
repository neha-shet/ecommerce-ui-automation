Feature: Shopping Cart functionality
  As an authenticated SauceDemo user
  I want to manage items in my shopping cart
  So that I can review, modify, and prepare my selected items for checkout

  Background:
    Given the user is logged in with valid credentials

  @smoke @regression
  Scenario: Add a product to cart
    When the user adds "Sauce Labs Backpack" to the cart
    Then the cart badge should show 1 item

  @regression
  Scenario: Add multiple products
    When the user adds "Sauce Labs Backpack" to the cart
    And the user adds "Sauce Labs Bike Light" to the cart
    And the user opens the cart
    Then the cart should contain 2 items
    And the cart should contain product "Sauce Labs Backpack"
    And the cart should contain product "Sauce Labs Bike Light"

  @regression
  Scenario: Verify cart contents
    When the user adds "Sauce Labs Backpack" to the cart
    And the user opens the cart
    Then the cart item "Sauce Labs Backpack" should display valid name, price, and quantity

  @regression
  Scenario: Remove a product
    When the user adds "Sauce Labs Backpack" to the cart
    And the user opens the cart
    And the user removes "Sauce Labs Backpack" from the cart
    Then "Sauce Labs Backpack" should no longer be displayed in the cart
    And the cart badge should show 0 items

  @regression
  Scenario: Navigate from products to cart
    When the user adds "Sauce Labs Backpack" to the cart
    And the user clicks the cart icon
    Then the Cart page should be displayed
