"""
Step definitions for checkout.feature scenarios.
"""

from behave import when, then, use_step_matcher
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

use_step_matcher("re")


@when(r'the user proceeds to checkout')
def step_user_proceeds_to_checkout(context):
    if not hasattr(context, "cart_page"):
        context.cart_page = CartPage(context.driver)
    context.cart_page.click_checkout()
    context.checkout_page = CheckoutPage(context.driver)
    assert context.checkout_page.is_on_checkout_info_page(), "Failed to navigate to Checkout Step One page"


@when(r'the user enters customer information "(?P<first_name>.*)", "(?P<last_name>.*)", "(?P<postal_code>.*)"')
def step_user_enters_customer_info(context, first_name, last_name, postal_code):
    if not hasattr(context, "checkout_page"):
        context.checkout_page = CheckoutPage(context.driver)
    context.checkout_page.enter_customer_info(first_name, last_name, postal_code)


@when(r'the user clicks continue')
def step_user_clicks_continue(context):
    if not hasattr(context, "checkout_page"):
        context.checkout_page = CheckoutPage(context.driver)
    context.checkout_page.click_continue()


@then(r'the checkout overview should display item "(?P<product_name>.*)"')
def step_verify_overview_item(context, product_name):
    if not hasattr(context, "checkout_page"):
        context.checkout_page = CheckoutPage(context.driver)
    assert context.checkout_page.is_on_checkout_overview_page(), "User is not on the Checkout Overview page"
    items = context.checkout_page.get_overview_item_names()
    assert product_name in items, f"Product '{product_name}' not found in overview item list {items}"


@then(r'the checkout calculations should be correct')
def step_verify_checkout_calculations(context):
    if not hasattr(context, "checkout_page"):
        context.checkout_page = CheckoutPage(context.driver)
    item_total = context.checkout_page.get_item_total()
    tax = context.checkout_page.get_tax()
    total = context.checkout_page.get_total()
    
    expected_total = round(item_total + tax, 2)
    assert abs(expected_total - total) < 0.01, (
        f"Checkout math mismatch: Item Total (${item_total}) + Tax (${tax}) = ${expected_total}, "
        f"but displayed Total is ${total}"
    )


@when(r'the user completes the order')
def step_user_completes_order(context):
    if not hasattr(context, "checkout_page"):
        context.checkout_page = CheckoutPage(context.driver)
    context.checkout_page.click_finish()


@then(r'the order confirmation "(?P<expected_msg>.*)" should be displayed')
def step_verify_order_confirmation(context, expected_msg):
    if not hasattr(context, "checkout_page"):
        context.checkout_page = CheckoutPage(context.driver)
    assert context.checkout_page.is_on_checkout_complete_page(), "User is not on the Checkout Complete page"
    actual_msg = context.checkout_page.get_confirmation_message()
    assert actual_msg == expected_msg, f"Expected confirmation message '{expected_msg}', got '{actual_msg}'"


@then(r'the checkout error message "(?P<expected_error>.*)" should be displayed')
def step_verify_checkout_error_message(context, expected_error):
    if not hasattr(context, "checkout_page"):
        context.checkout_page = CheckoutPage(context.driver)
    actual_error = context.checkout_page.get_error_message()
    assert expected_error in actual_error, f"Expected error '{expected_error}', but got '{actual_error}'"
