Feature: Product Catalog functionality
  As an authenticated SauceDemo user
  I want to browse, sort, and inspect products in the catalog
  So that I can select items to purchase

  Background:
    Given the user is logged in with valid credentials

  @smoke @regression
  Scenario: Verify products are displayed
    When the user is on the Products page
    Then the Products page should be displayed
    And products should be visible

  @regression
  Scenario: Verify product names
    When the user is on the Products page
    Then at least one product should be displayed
    And every displayed product should have a non-empty name

  @regression
  Scenario: Verify product prices
    When the user is on the Products page
    Then every displayed product should have a valid price greater than zero

  @regression
  Scenario: Sort products by price low to high
    When the user is on the Products page
    And the user sorts products by "Price (low to high)"
    Then the products should be sorted by price in ascending order

  @regression
  Scenario: Sort products by price high to low
    When the user is on the Products page
    And the user sorts products by "Price (high to low)"
    Then the products should be sorted by price in descending order

  @regression
  Scenario: Open product details
    When the user is on the Products page
    And the user clicks on the first product
    Then the product details page should be displayed with valid details
