"""
Step definitions for products.feature scenarios.
"""

from behave import given, when, then, use_step_matcher
from pages.login_page import LoginPage
from pages.products_page import ProductsPage

use_step_matcher("re")


@given(r'the user is logged in with valid credentials')
def step_user_logged_in_valid_credentials(context):
    login_page = LoginPage(context.driver)
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")
    
    context.products_page = ProductsPage(context.driver)
    assert context.products_page.is_on_products_page(), "Failed to log in to Products page"


@when(r'the user is on the Products page')
def step_user_is_on_products_page(context):
    if not hasattr(context, "products_page"):
        context.products_page = ProductsPage(context.driver)
    assert context.products_page.is_on_products_page(), "User is not on the Products page"


@then(r'products should be visible')
def step_products_visible(context):
    count = context.products_page.get_product_count()
    assert count > 0, f"Expected at least 1 product visible, got {count}"


@then(r'at least one product should be displayed')
def step_at_least_one_product_displayed(context):
    count = context.products_page.get_product_count()
    assert count > 0, "No products are displayed"


@then(r'every displayed product should have a non-empty name')
def step_every_product_has_non_empty_name(context):
    names = context.products_page.get_product_names()
    assert len(names) > 0, "No product names retrieved"
    for name in names:
        assert name and len(name.strip()) > 0, f"Found empty product name in {names}"


@then(r'every displayed product should have a valid price greater than zero')
def step_every_product_has_valid_price(context):
    prices = context.products_page.get_product_prices()
    assert len(prices) > 0, "No product prices retrieved"
    for price in prices:
        assert isinstance(price, float), f"Price {price} is not a valid float"
        assert price > 0.0, f"Expected price > 0, got {price}"


@when(r'the user sorts products by "(?P<option_text>.*)"')
def step_user_sorts_products_by(context, option_text):
    context.products_page.sort_products_by(option_text)


@then(r'the products should be sorted by price in ascending order')
def step_verify_products_sorted_ascending(context):
    actual_prices = context.products_page.get_product_prices()
    expected_prices = sorted(actual_prices)
    assert actual_prices == expected_prices, f"Prices not sorted low to high. Actual: {actual_prices}, Expected: {expected_prices}"


@then(r'the products should be sorted by price in descending order')
def step_verify_products_sorted_descending(context):
    actual_prices = context.products_page.get_product_prices()
    expected_prices = sorted(actual_prices, reverse=True)
    assert actual_prices == expected_prices, f"Prices not sorted high to low. Actual: {actual_prices}, Expected: {expected_prices}"


@when(r'the user clicks on the first product')
def step_user_clicks_first_product(context):
    context.selected_product_name = context.products_page.click_first_product()


@then(r'the product details page should be displayed with valid details')
def step_verify_product_details(context):
    details = context.products_page.get_product_detail_info()
    
    assert details["name"] == context.selected_product_name, f"Expected product name '{context.selected_product_name}', got '{details['name']}'"
    assert details["price"] > 0.0, f"Expected detail price > 0, got {details['price']}"
    assert len(details["description"]) > 0, "Product detail description is empty"
    assert details["image_src"] and len(details["image_src"]) > 0, "Product detail image source is missing"
