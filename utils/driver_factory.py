"""
WebDriver Factory module for initializing and configuring Selenium WebDriver instances.
Uses Selenium 4 built-in Selenium Manager for automated browser driver lifecycle.
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from utils import config

def get_driver(headless: bool = None) -> webdriver.Chrome:
    """
    Initializes and returns a configured Chrome WebDriver instance.
    
    :param headless: Optional boolean to override default headless mode from config.
    :return: Configured Selenium Chrome WebDriver instance.
    """
    if headless is None:
        headless = config.HEADLESS
        
    chrome_options = Options()
    
    if headless:
        chrome_options.add_argument("--headless=new")
    
    # Standard Chrome flags for headless & automated stability
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--disable-search-engine-choice-screen")

    # Selenium 4 automatically manages ChromeDriver binary via Selenium Manager
    driver = webdriver.Chrome(options=chrome_options)
    
    if not headless:
        driver.maximize_window()
        
    return driver

def quit_driver(driver: webdriver.Chrome) -> None:
    """
    Safely quits the WebDriver instance if active.
    
    :param driver: Chrome WebDriver instance to close.
    """
    if driver:
        try:
            driver.quit()
        except Exception:
            pass
