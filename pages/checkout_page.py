"""
Page Object for SauceDemo Checkout Pages (Step One, Step Two Overview, and Complete).
Encapsulates locators and interaction methods for customer info entry, summary validation, and order completion.
"""

from typing import List
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils import config


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, config.DEFAULT_TIMEOUT)

        # Locators - Step One (Customer Information)
        self.first_name_input = (By.ID, "first-name")
        self.last_name_input = (By.ID, "last-name")
        self.postal_code_input = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")
        self.error_message_container = (By.CSS_SELECTOR, "h3[data-test='error']")

        # Locators - Step Two (Overview & Summary)
        self.subtotal_label = (By.CLASS_NAME, "summary_subtotal_label")
        self.tax_label = (By.CLASS_NAME, "summary_tax_label")
        self.total_label = (By.CLASS_NAME, "summary_total_label")
        self.overview_item_names = (By.CLASS_NAME, "inventory_item_name")
        self.finish_button = (By.ID, "finish")

        # Locators - Checkout Complete
        self.complete_header = (By.CLASS_NAME, "complete-header")
        self.complete_text = (By.CLASS_NAME, "complete-text")
        self.back_home_button = (By.ID, "back-to-products")

    # --- Step One Methods ---
    def is_on_checkout_info_page(self) -> bool:
        """Verifies if currently on Checkout Step One page."""
        try:
            self.wait.until(EC.url_contains("checkout-step-one.html"))
            self.wait.until(EC.presence_of_element_located(self.continue_button))
            return True
        except Exception:
            return False

    def enter_first_name(self, first_name: str):
        """Enters first name into the checkout input field."""
        elem = self.wait.until(EC.presence_of_element_located(self.first_name_input))
        elem.clear()
        if first_name:
            elem.send_keys(first_name)

    def enter_last_name(self, last_name: str):
        """Enters last name into the checkout input field."""
        elem = self.wait.until(EC.presence_of_element_located(self.last_name_input))
        elem.clear()
        if last_name:
            elem.send_keys(last_name)

    def enter_postal_code(self, postal_code: str):
        """Enters postal code into the checkout input field."""
        elem = self.wait.until(EC.presence_of_element_located(self.postal_code_input))
        elem.clear()
        if postal_code:
            elem.send_keys(postal_code)

    def enter_customer_info(self, first_name: str, last_name: str, postal_code: str):
        """Fills out the entire checkout customer information form."""
        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.enter_postal_code(postal_code)

    def click_continue(self):
        """Clicks the Continue button and waits for step two navigation or error message."""
        btn = self.wait.until(EC.element_to_be_clickable(self.continue_button))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", btn)
        self.driver.execute_script("arguments[0].click();", btn)
        WebDriverWait(self.driver, config.DEFAULT_TIMEOUT).until(
            lambda d: "checkout-step-two.html" in d.current_url or len(d.find_elements(By.CSS_SELECTOR, "h3[data-test='error']")) > 0
        )

    def get_error_message(self) -> str:
        """Returns the displayed error message text on checkout info page."""
        error_elem = self.wait.until(EC.visibility_of_element_located(self.error_message_container))
        return error_elem.text.strip()

    # --- Step Two Overview Methods ---
    def is_on_checkout_overview_page(self) -> bool:
        """Verifies if currently on Checkout Step Two Overview page."""
        try:
            self.wait.until(EC.url_contains("checkout-step-two.html"))
            self.wait.until(EC.presence_of_element_located(self.finish_button))
            return True
        except Exception:
            return False

    def get_overview_item_names(self) -> List[str]:
        """Returns a list of item names displayed in the checkout overview."""
        elements = self.wait.until(EC.presence_of_all_elements_located(self.overview_item_names))
        return [elem.text.strip() for elem in elements]

    def get_item_total(self) -> float:
        """Parses and returns numeric Item Total (subtotal) from summary."""
        label_text = self.wait.until(EC.presence_of_element_located(self.subtotal_label)).text
        val = label_text.split("$")[1].strip()
        return float(val)

    def get_tax(self) -> float:
        """Parses and returns numeric Tax amount from summary."""
        label_text = self.wait.until(EC.presence_of_element_located(self.tax_label)).text
        val = label_text.split("$")[1].strip()
        return float(val)

    def get_total(self) -> float:
        """Parses and returns numeric Final Total amount from summary."""
        label_text = self.wait.until(EC.presence_of_element_located(self.total_label)).text
        val = label_text.split("$")[1].strip()
        return float(val)

    def click_finish(self):
        """Clicks the Finish button to complete the order and waits for Checkout Complete URL."""
        btn = self.wait.until(EC.element_to_be_clickable(self.finish_button))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", btn)
        self.driver.execute_script("arguments[0].click();", btn)
        self.wait.until(EC.url_contains("checkout-complete.html"))

    # --- Checkout Complete Methods ---
    def is_on_checkout_complete_page(self) -> bool:
        """Verifies if currently on Checkout Complete page."""
        try:
            self.wait.until(EC.url_contains("checkout-complete.html"))
            self.wait.until(EC.presence_of_element_located(self.complete_header))
            return True
        except Exception:
            return False

    def get_confirmation_message(self) -> str:
        """Returns the confirmation header message (e.g. 'Thank you for your order!')."""
        header_elem = self.wait.until(EC.presence_of_element_located(self.complete_header))
        return header_elem.text.strip()
