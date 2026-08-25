"""
Page Object for SauceDemo Login Page.
Contains locators and interaction methods for logging into the application and validating error states.
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils import config


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, config.DEFAULT_TIMEOUT)

        # Locators
        self.username_input = (By.ID, "user-name")
        self.password_input = (By.ID, "password")
        self.login_button = (By.ID, "login-button")
        self.error_message_container = (By.CSS_SELECTOR, "h3[data-test='error']")

    def navigate(self):
        """Navigates to the login page base URL."""
        self.driver.get(config.BASE_URL)
        self.wait_for_page_load()

    def wait_for_page_load(self):
        """Waits for the login page elements to be visible."""
        self.wait.until(EC.visibility_of_element_located(self.login_button))

    def is_on_login_page(self) -> bool:
        """Checks if currently on the login page."""
        try:
            return self.driver.find_element(*self.login_button).is_displayed()
        except Exception:
            return False

    def enter_username(self, username: str):
        """Enters the username into the username field."""
        user_field = self.wait.until(EC.visibility_of_element_located(self.username_input))
        user_field.clear()
        if username:
            user_field.send_keys(username)

    def enter_password(self, password: str):
        """Enters the password into the password field."""
        pass_field = self.wait.until(EC.visibility_of_element_located(self.password_input))
        pass_field.clear()
        if password:
            pass_field.send_keys(password)

    def click_login(self):
        """Clicks the login button."""
        btn = self.wait.until(EC.element_to_be_clickable(self.login_button))
        btn.click()

    def login(self, username: str, password: str):
        """Helper method to perform full login sequence."""
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def get_error_message(self) -> str:
        """Returns the text of the displayed login error message."""
        error_element = self.wait.until(
            EC.visibility_of_element_located(self.error_message_container)
        )
        return error_element.text
