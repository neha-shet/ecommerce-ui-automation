"""
Behave environment hooks file.
Manages WebDriver lifecycle, automatic failure screenshots, and test reporting setup.
"""

import os
import re
from datetime import datetime
from utils import driver_factory, config


def before_scenario(context, scenario):
    """Initializes WebDriver instance before each scenario."""
    context.driver = driver_factory.get_driver()


def after_scenario(context, scenario):
    """
    Hook executed after each scenario.
    Captures screenshot on scenario failure or error BEFORE closing WebDriver.
    """
    if hasattr(context, "driver") and context.driver:
        scenario_failed = False
        if hasattr(scenario, "status"):
            status_str = str(scenario.status).lower()
            if "failed" in status_str or "error" in status_str:
                scenario_failed = True

        if scenario_failed:
            try:
                os.makedirs(config.SCREENSHOTS_DIR, exist_ok=True)
                
                # Sanitize feature and scenario names for filename
                feature_name = re.sub(r"[^\w\-]", "_", scenario.feature.name.lower())
                scenario_name = re.sub(r"[^\w\-]", "_", scenario.name.lower())
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                
                filename = f"{feature_name}_{scenario_name}_{timestamp}.png"
                filepath = os.path.join(config.SCREENSHOTS_DIR, filename)
                
                context.driver.save_screenshot(filepath)
                print(f"\n[FAILURE SCREENSHOT CAPTURED] {filepath}")
            except Exception as e:
                print(f"\n[ERROR CAPTURING SCREENSHOT] {e}")

        # Cleanly terminate browser session
        driver_factory.quit_driver(context.driver)
