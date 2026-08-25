"""
Step definitions for cart.feature scenarios.
"""

from behave import when, then, use_step_matcher
from pages.products_page import ProductsPage
from pages.cart_page import CartPage

use_step_matcher("re")


@when(r'the user adds "(?P<product_name>.*)" to the cart')
def step_user_adds_product_to_cart(context, product_name):
    if not hasattr(context, "products_page"):
        context.products_page = ProductsPage(context.driver)
    context.products_page.add_product_to_cart(product_name)


@then(r'the cart badge should show (?P<expected_count>\d+) item(?:s)?')
def step_verify_cart_badge_count(context, expected_count):
    if not hasattr(context, "products_page"):
        context.products_page = ProductsPage(context.driver)
    actual_count = context.products_page.get_cart_badge_count()
    assert actual_count == int(expected_count), f"Expected cart badge count {expected_count}, got {actual_count}"


@when(r'the user opens the cart')
@when(r'the user clicks the cart icon')
def step_user_opens_cart(context):
    if not hasattr(context, "products_page"):
        context.products_page = ProductsPage(context.driver)
    context.products_page.click_cart_icon()
    context.cart_page = CartPage(context.driver)
    assert context.cart_page.is_on_cart_page(), "Failed to navigate to Cart page"


@then(r'the cart should contain (?P<expected_count>\d+) item(?:s)?')
def step_verify_cart_item_count(context, expected_count):
    if not hasattr(context, "cart_page"):
        context.cart_page = CartPage(context.driver)
    actual_count = context.cart_page.get_cart_item_count()
    assert actual_count == int(expected_count), f"Expected {expected_count} items in cart, found {actual_count}"


@then(r'the cart should contain product "(?P<product_name>.*)"')
def step_verify_cart_contains_product(context, product_name):
    if not hasattr(context, "cart_page"):
        context.cart_page = CartPage(context.driver)
    names = context.cart_page.get_cart_item_names()
    assert product_name in names, f"Product '{product_name}' not found in cart list {names}"


@then(r'the cart item "(?P<product_name>.*)" should display valid name, price, and quantity')
def step_verify_cart_item_details(context, product_name):
    if not hasattr(context, "cart_page"):
        context.cart_page = CartPage(context.driver)
    details = context.cart_page.get_cart_item_details(product_name)
    assert details["name"] == product_name, f"Expected item name '{product_name}', got '{details['name']}'"
    assert details["price"] > 0.0, f"Expected item price > 0, got {details['price']}"
    assert details["quantity"] >= 1, f"Expected item quantity >= 1, got {details['quantity']}"


@when(r'the user removes "(?P<product_name>.*)" from the cart')
def step_user_removes_product_from_cart(context, product_name):
    if not hasattr(context, "cart_page"):
        context.cart_page = CartPage(context.driver)
    context.cart_page.remove_product_by_name(product_name)


@then(r'"(?P<product_name>.*)" should no longer be displayed in the cart')
def step_verify_product_removed_from_cart(context, product_name):
    if not hasattr(context, "cart_page"):
        context.cart_page = CartPage(context.driver)
    names = context.cart_page.get_cart_item_names()
    assert product_name not in names, f"Product '{product_name}' is still displayed in cart: {names}"


@then(r'the Cart page should be displayed')
def step_verify_cart_page_displayed(context):
    if not hasattr(context, "cart_page"):
        context.cart_page = CartPage(context.driver)
    assert context.cart_page.is_on_cart_page(), "Cart page is not displayed"
