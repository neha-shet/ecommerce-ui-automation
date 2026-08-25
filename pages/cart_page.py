"""
Page Object for SauceDemo Shopping Cart Page (cart.html).
Encapsulates locators and interaction methods for inspecting cart items, removing items, and checkout navigation.
"""

from typing import List, Dict
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils import config


class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, config.DEFAULT_TIMEOUT)

        # Locators
        self.page_title = (By.CLASS_NAME, "title")
        self.cart_items = (By.CLASS_NAME, "cart_item")
        self.item_names = (By.CLASS_NAME, "inventory_item_name")
        self.item_prices = (By.CLASS_NAME, "inventory_item_price")
        self.item_quantities = (By.CLASS_NAME, "cart_quantity")
        self.checkout_button = (By.ID, "checkout")
        self.continue_shopping_button = (By.ID, "continue-shopping")

    def is_on_cart_page(self) -> bool:
        """Verifies if the user is currently on the Cart page."""
        try:
            self.wait.until(EC.url_contains("cart.html"))
            title_elem = self.wait.until(EC.visibility_of_element_located(self.page_title))
            return title_elem.text == "Your Cart"
        except Exception:
            return False

    def get_cart_item_count(self) -> int:
        """Returns the total number of items currently in the cart."""
        items = self.driver.find_elements(*self.cart_items)
        return len(items)

    def get_cart_item_names(self) -> List[str]:
        """Returns a list of names of all items in the cart."""
        elements = self.driver.find_elements(*self.item_names)
        return [elem.text.strip() for elem in elements if elem.is_displayed()]

    def get_cart_item_details(self, product_name: str) -> Dict:
        """Returns a dictionary containing quantity, name, and price for a specific product in cart."""
        items = self.wait.until(EC.presence_of_all_elements_located(self.cart_items))
        for item in items:
            name_elem = item.find_element(By.CLASS_NAME, "inventory_item_name")
            if name_elem.text.strip() == product_name:
                price_str = item.find_element(By.CLASS_NAME, "inventory_item_price").text.strip()
                qty_str = item.find_element(By.CLASS_NAME, "cart_quantity").text.strip()
                price = float(price_str.replace("$", "").strip())
                qty = int(qty_str)
                return {
                    "name": product_name,
                    "price_str": price_str,
                    "price": price,
                    "quantity": qty
                }
        raise ValueError(f"Product '{product_name}' not found in cart.")

    def remove_product_by_name(self, product_name: str):
        """Removes a product from the cart by clicking its Remove button."""
        items = self.wait.until(EC.presence_of_all_elements_located(self.cart_items))
        for item in items:
            name_elem = item.find_element(By.CLASS_NAME, "inventory_item_name")
            if name_elem.text.strip() == product_name:
                btn = item.find_element(By.TAG_NAME, "button")
                self.driver.execute_script("arguments[0].click();", btn)
                return
        raise ValueError(f"Cannot remove product '{product_name}': not found in cart.")

    def click_checkout(self):
        """Clicks the Checkout button on the Cart page and waits for Checkout Step One URL."""
        btn = self.wait.until(EC.element_to_be_clickable(self.checkout_button))
        self.driver.execute_script("arguments[0].click();", btn)
        self.wait.until(EC.url_contains("checkout-step-one.html"))

    def click_continue_shopping(self):
        """Clicks the Continue Shopping button on the Cart page."""
        btn = self.wait.until(EC.element_to_be_clickable(self.continue_shopping_button))
        self.driver.execute_script("arguments[0].click();", btn)
