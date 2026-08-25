"""
Configuration file for application URLs, timeouts, browser settings, and report paths.
"""

import os

BASE_URL = "https://www.saucedemo.com/"
DEFAULT_TIMEOUT = 10  # seconds for explicit waits
BROWSER = "chrome"
HEADLESS = True  # set to False for visual browser execution

# Directory paths for test artifacts
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCREENSHOTS_DIR = os.path.join(PROJECT_ROOT, "screenshots")
REPORTS_DIR = os.path.join(PROJECT_ROOT, "reports")
