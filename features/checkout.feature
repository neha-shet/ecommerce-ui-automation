Feature: Checkout functionality
  As an authenticated SauceDemo user
  I want to enter my shipping information and review my order
  So that I can successfully complete my purchase

  Background:
    Given the user is logged in with valid credentials

  @smoke @regression
  Scenario: Successful checkout
    When the user adds "Sauce Labs Backpack" to the cart
    And the user opens the cart
    And the user proceeds to checkout
    And the user enters customer information "Neha", "Shet", "560001"
    And the user clicks continue
    Then the checkout overview should display item "Sauce Labs Backpack"
    And the checkout calculations should be correct
    When the user completes the order
    Then the order confirmation "Thank you for your order!" should be displayed

  @regression
  Scenario: Missing first name
    When the user adds "Sauce Labs Backpack" to the cart
    And the user opens the cart
    And the user proceeds to checkout
    And the user enters customer information "", "Shet", "560001"
    And the user clicks continue
    Then the checkout error message "Error: First Name is required" should be displayed

  @regression
  Scenario: Missing last name
    When the user adds "Sauce Labs Backpack" to the cart
    And the user opens the cart
    And the user proceeds to checkout
    And the user enters customer information "Neha", "", "560001"
    And the user clicks continue
    Then the checkout error message "Error: Last Name is required" should be displayed

  @regression
  Scenario: Missing postal code
    When the user adds "Sauce Labs Backpack" to the cart
    And the user opens the cart
    And the user proceeds to checkout
    And the user enters customer information "Neha", "Shet", ""
    And the user clicks continue
    Then the checkout error message "Error: Postal Code is required" should be displayed
