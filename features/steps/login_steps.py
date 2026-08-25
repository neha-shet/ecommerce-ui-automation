"""
Step definitions for login.feature scenarios.
"""

from behave import given, when, then, use_step_matcher
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage
from utils import config

# Use regex step matcher to support empty string parameters cleanly
use_step_matcher("re")


@given(r'the user is on the SauceDemo login page')
def step_user_on_login_page(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.navigate()


@when(r'the user enters username "(?P<username>.*)" and password "(?P<password>.*)"')
def step_user_enters_credentials(context, username, password):
    context.login_page.enter_username(username)
    context.login_page.enter_password(password)


@when(r'the user enters valid credentials')
def step_user_enters_valid_credentials(context):
    context.login_page.enter_username("standard_user")
    context.login_page.enter_password("secret_sauce")


@when(r'the user clicks the login button')
def step_user_clicks_login_button(context):
    context.login_page.click_login()


@then(r'the Products page should be displayed')
def step_products_page_should_be_displayed(context):
    wait = WebDriverWait(context.driver, config.DEFAULT_TIMEOUT)
    wait.until(EC.url_contains("inventory.html"))
    title_element = wait.until(
        EC.visibility_of_element_located((By.CLASS_NAME, "title"))
    )
    assert title_element.text == "Products", f"Expected header 'Products', got '{title_element.text}'"


@then(r'the login error message "(?P<expected_error>.*)" should be displayed')
def step_verify_login_error_message(context, expected_error):
    actual_error = context.login_page.get_error_message()
    assert expected_error in actual_error, f"Expected error '{expected_error}', but got '{actual_error}'"
