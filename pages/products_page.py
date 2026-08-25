"""
Page Object for SauceDemo Products Page and Product Details Page.
Encapsulates locators and interaction methods for browsing, sorting, viewing, and adding products to cart.
"""

from typing import List
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from utils import config


class ProductsPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, config.DEFAULT_TIMEOUT)

        # Locators - Products Catalog
        self.page_title = (By.CLASS_NAME, "title")
        self.inventory_container = (By.ID, "inventory_container")
        self.inventory_items = (By.CLASS_NAME, "inventory_item")
        self.item_names = (By.CLASS_NAME, "inventory_item_name")
        self.item_prices = (By.CLASS_NAME, "inventory_item_price")
        self.sort_select = (By.CLASS_NAME, "product_sort_container")
        self.cart_link = (By.CLASS_NAME, "shopping_cart_link")
        self.cart_badge = (By.CLASS_NAME, "shopping_cart_badge")

        # Locators - Product Details
        self.detail_name = (By.CLASS_NAME, "inventory_details_name")
        self.detail_price = (By.CLASS_NAME, "inventory_details_price")
        self.detail_desc = (By.CLASS_NAME, "inventory_details_desc")
        self.detail_img = (By.CLASS_NAME, "inventory_details_img")
        self.back_to_products_btn = (By.ID, "back-to-products")

    def is_on_products_page(self) -> bool:
        """Verifies if the user is currently on the Products page."""
        try:
            self.wait.until(EC.url_contains("inventory.html"))
            title_elem = self.wait.until(EC.visibility_of_element_located(self.page_title))
            return title_elem.text == "Products"
        except Exception:
            return False

    def get_product_count(self) -> int:
        """Returns the number of displayed products."""
        items = self.wait.until(EC.presence_of_all_elements_located(self.inventory_items))
        return len(items)

    def get_product_names(self) -> List[str]:
        """Returns a list of all displayed product names."""
        elements = self.wait.until(EC.presence_of_all_elements_located(self.item_names))
        return [elem.text.strip() for elem in elements]

    def get_product_prices_raw(self) -> List[str]:
        """Returns a list of raw price strings (e.g., '$29.99')."""
        elements = self.wait.until(EC.presence_of_all_elements_located(self.item_prices))
        return [elem.text.strip() for elem in elements]

    def get_product_prices(self) -> List[float]:
        """Returns a list of parsed numeric product prices (e.g., 29.99)."""
        raw_prices = self.get_product_prices_raw()
        prices = []
        for p in raw_prices:
            clean_price = p.replace("$", "").strip()
            prices.append(float(clean_price))
        return prices

    def sort_products_by(self, option_text: str):
        """
        Selects a sorting option from the product sort dropdown.
        Option examples: 'Price (low to high)', 'Price (high to low)'
        """
        select_elem = self.wait.until(EC.element_to_be_clickable(self.sort_select))
        select = Select(select_elem)
        
        option_map = {
            "Price (low to high)": "lohi",
            "Price (high to low)": "hilo",
            "Name (A to Z)": "az",
            "Name (Z to A)": "za"
        }
        
        if option_text in option_map:
            select.select_by_value(option_map[option_text])
        else:
            select.select_by_visible_text(option_text)

    def add_product_to_cart(self, product_name: str):
        """Adds a specific product to the shopping cart by product name."""
        items = self.wait.until(EC.presence_of_all_elements_located(self.inventory_items))
        for item in items:
            name_elem = item.find_element(By.CLASS_NAME, "inventory_item_name")
            if name_elem.text.strip() == product_name:
                btn = item.find_element(By.TAG_NAME, "button")
                self.driver.execute_script("arguments[0].click();", btn)
                return
        raise ValueError(f"Product '{product_name}' not found on Products page.")

    def get_cart_badge_count(self) -> int:
        """Returns the integer count displayed on the shopping cart badge, or 0 if empty."""
        badges = self.driver.find_elements(*self.cart_badge)
        if not badges or not badges[0].is_displayed():
            return 0
        return int(badges[0].text.strip())

    def click_cart_icon(self):
        """Clicks the shopping cart icon in the top header."""
        icon = self.wait.until(EC.element_to_be_clickable(self.cart_link))
        self.driver.execute_script("arguments[0].click();", icon)

    def click_first_product(self) -> str:
        """Clicks the first product in the list and returns its name."""
        names = self.get_product_names()
        if not names:
            raise ValueError("No products found to click.")
        first_name = names[0]
        self.click_product_by_name(first_name)
        return first_name

    def click_product_by_name(self, product_name: str):
        """Clicks on a product link by its exact name to navigate to details page."""
        elements = self.wait.until(EC.presence_of_all_elements_located(self.item_names))
        for elem in elements:
            if elem.text.strip() == product_name:
                self.driver.execute_script("arguments[0].click();", elem)
                return
        raise ValueError(f"Product '{product_name}' not found on page.")

    def get_product_detail_info(self) -> dict:
        """Retrieves details from the Product Detail view."""
        name = self.wait.until(EC.visibility_of_element_located(self.detail_name)).text.strip()
        price_str = self.wait.until(EC.visibility_of_element_located(self.detail_price)).text.strip()
        desc = self.wait.until(EC.visibility_of_element_located(self.detail_desc)).text.strip()
        img_elem = self.wait.until(EC.visibility_of_element_located(self.detail_img))
        img_src = img_elem.get_attribute("src")
        
        price = float(price_str.replace("$", "").strip())
        
        return {
            "name": name,
            "price_str": price_str,
            "price": price,
            "description": desc,
            "image_src": img_src
        }

    def click_back_to_products(self):
        """Clicks the 'Back to products' button on the detail page."""
        btn = self.wait.until(EC.element_to_be_clickable(self.back_to_products_btn))
        self.driver.execute_script("arguments[0].click();", btn)
