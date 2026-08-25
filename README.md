# E-Commerce UI Automation Suite

A professional, industrial-grade BDD-based UI automation framework built with Python, Selenium WebDriver, and Behave for automated testing of an e-commerce web application.

---

## Overview

This project demonstrates an end-to-end QA Automation framework designed according to software testing industry best practices. It showcases:

- **UI Automation**: Robust web element interaction using explicit waits and modern Selenium WebDriver practices.
- **Behavior-Driven Development (BDD)**: Clear, business-readable Gherkin feature files separating specifications from step implementations.
- **Page Object Model (POM)**: High maintainability and reusability by encapsulating page locators and interaction logic inside page classes.
- **Functional Testing**: End-to-end user journeys from user authentication to product selection, cart management, and order checkout.
- **Positive & Negative Testing**: Verification of valid functional flows as well as edge cases, field validations, and error handling.
- **Smoke & Regression Testing**: Structured test suite categorization using `@smoke` and `@regression` tags.
- **Test Reporting & Failure Diagnostics**: Standalone HTML test execution reports and automatic failure screenshot capture.
- **Git-Based Development**: Clean repository architecture, version control, and CI/CD-ready structure.

---

## Application Under Test

- **Target Application**: SauceDemo / Swag Labs
- **URL**: `https://www.saucedemo.com/`
- **Description**: A representative e-commerce demo application providing standard online shopping features including authentication, catalog browsing, price sorting, item selection, shopping cart management, customer information entry, and checkout confirmation.

---

## Tech Stack

- **Programming Language**: Python 3
- **Automation Tool**: Selenium WebDriver 4
- **BDD Framework**: Behave 1.3
- **Specification Language**: Gherkin
- **Design Pattern**: Page Object Model (POM)
- **Reporting Plugin**: Behave HTML Formatter (`behave-html-formatter`)
- **Version Control**: Git / GitHub

---

## Framework Architecture

The framework follows a modular, decoupled architecture:

- **`features/`**: Contains Gherkin feature specification files (`.feature`) and test environment hooks (`environment.py`).
- **`features/steps/`**: Contains Behave step definition Python files connecting Gherkin scenarios to Page Object logic.
- **`pages/`**: Encapsulates all page locators and UI interaction methods inside dedicated Page Object classes.
- **`utils/`**: Houses central configuration (`config.py`) and browser session creation helpers (`driver_factory.py`).
- **`reports/`**: Destination directory for generated HTML test execution reports.
- **`screenshots/`**: Destination directory for automatically captured failure screenshots.

---

## Test Coverage

| Feature Component | Scenarios | Total Steps | Description |
| :--- | :---: | :---: | :--- |
| **Login** | 6 | 24 | Positive login, invalid credentials, empty fields, locked-out user |
| **Product Catalog** | 6 | 23 | Catalog display, non-empty names, valid prices, price sorting, product details |
| **Shopping Cart** | 5 | 24 | Single & multiple additions, badge count, item details, removal, navigation |
| **Checkout** | 4 | 31 | Successful checkout journey, subtotal/tax/total math verification, field validations |
| **Total Suite** | **21** | **102** | **100% Passing Automated Tests** |

---

## Test Types & Categorization

### 1. Smoke Testing (`@smoke`)
Contains 4 critical happy-path scenarios representing the core end-to-end user workflow:
- Valid login
- Product catalog display
- Adding a product to cart
- Completing order checkout

### 2. Regression Testing (`@regression`)
Encompasses the complete 21-scenario test suite to ensure existing features remain defect-free after changes.

### 3. Positive Testing
Validates expected system behavior for standard user workflows (valid credentials, sorting, cart management, successful purchase).

### 4. Negative Testing
Validates application resilience against invalid inputs (invalid usernames/passwords, locked-out accounts, missing checkout first name/last name/postal code).

---

## Test Scenarios Summary

- **Authentication**: Valid login (`standard_user`), invalid credentials, empty inputs, locked-out user handling.
- **Product Catalog**: Verification of product listings, name validity, non-zero pricing, ascending/descending price sorting (`low to high`, `high to low`), and product detail modal metadata.
- **Shopping Cart**: Item addition, badge counter updates, cart contents inspection (name, price, quantity), item removal, and catalog-to-cart header navigation.
- **Checkout Workflow**: Full checkout flow, customer info submission, exact subtotal + tax = total math validation, order completion confirmation (`"Thank you for your order!"`), and missing field validation errors.

---

## Project Structure

```text
ecommerce-ui-automation/
│
├── features/
│   ├── environment.py         # Behave hooks for driver lifecycle & failure screenshots
│   ├── login.feature          # Login authentication Gherkin scenarios
│   ├── products.feature       # Product catalog & sorting Gherkin scenarios
│   ├── cart.feature           # Shopping cart operations Gherkin scenarios
│   ├── checkout.feature       # Checkout & order confirmation Gherkin scenarios
│   └── steps/
│       ├── login_steps.py     # Login step definition bindings
│       ├── products_steps.py  # Products step definition bindings
│       ├── cart_steps.py      # Cart step definition bindings
│       └── checkout_steps.py  # Checkout step definition bindings
│
├── pages/
│   ├── login_page.py          # Page Object for Login page
│   ├── products_page.py       # Page Object for Products Catalog & Details
│   ├── cart_page.py           # Page Object for Shopping Cart page
│   └── checkout_page.py       # Page Object for Checkout Step One, Two, and Complete
│
├── utils/
│   ├── config.py              # Centralized configuration (URLs, timeouts, paths)
│   └── driver_factory.py      # Selenium WebDriver creation & management
│
├── reports/                   # HTML execution reports (excluded from git)
│   └── .gitkeep
├── screenshots/               # Automatic failure screenshots (excluded from git)
│   └── .gitkeep
│
├── .gitignore                 # Git ignore file for environment & generated files
├── behave.ini                 # Behave runner configuration & formatters
├── requirements.txt           # Python dependency specifications
└── README.md                  # Professional project documentation
```

---

## Installation & Setup

### Prerequisites
- Python 3.10+ installed
- Google Chrome browser installed
- Git version control installed

### Step-by-Step Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/nehajshet/ecommerce-ui-automation.git
   cd ecommerce-ui-automation
   ```

2. **Create a Python virtual environment**:
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**:
   - On Windows (PowerShell):
     ```powershell
     .\venv\Scripts\Activate.ps1
     ```
   - On Windows (Command Prompt):
     ```cmd
     .\venv\Scripts\activate.bat
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

---

## Running Tests

### Run Full Test Suite
```bash
python -m behave
```

### Run Smoke Tests Only
```bash
python -m behave --tags=smoke
```

### Run Regression Tests Only
```bash
python -m behave --tags=regression
```

### Generate HTML Test Execution Report
```bash
python -m behave -f html -o reports/behave_report.html
```

---

## Test Reports

- HTML test execution reports are automatically generated into `reports/behave_report.html`.
- The report presents an interactive breakdown of executed features, scenarios, step execution status, and timing.
- Generated HTML reports are excluded from Git repository tracking via `.gitignore` to maintain clean source control.

---

## Failure Screenshots

- The framework automatically captures a browser screenshot whenever a test scenario fails.
- Screenshots are saved in the `screenshots/` directory using the naming convention:
  ```text
  screenshots/{feature_name}_{scenario_name}_{timestamp}.png
  ```
- Failure screenshot capture occurs inside the `after_scenario` hook in `features/environment.py` **before** the browser session is closed.
- Screenshot artifacts are excluded from Git repository tracking via `.gitignore`.

---

## Design Patterns

### Page Object Model (POM)
The framework strictly adheres to the Page Object Model design pattern:
- **Separation of Concerns**: Test logic (`features/` and `steps/`) is completely decoupled from UI element locators and interaction details (`pages/`).
- **Maintainability**: Web element locators are maintained in a single location per page class. UI updates require changes only in the corresponding Page Object class.
- **Reusability**: Page Object methods (e.g., `login()`, `add_product_to_cart()`, `enter_customer_info()`) are reused across multiple test scenarios.

---

## QA Practices Demonstrated

- **Software Testing Life Cycle (STLC)**: Requirements analysis, scenario design, test implementation, execution, and reporting.
- **Test Scenario Design**: Comprehensive coverage of happy paths, error boundaries, and negative test cases.
- **Explicit Waits**: Avoidance of hardcoded delays (`time.sleep()`), using `WebDriverWait` and `expected_conditions` for dynamic synchronization.
- **Assertion Standards**: Strong assertion checks for titles, error banners, badge counts, item lists, and numeric financial calculations.
- **Defect-Oriented Diagnostics**: Automatic failure screenshot generation and detailed logging.
- **Clean Code & Reusability**: DRY principles, explicit step definitions, and centralized configuration.

---

## Future Enhancements

The framework is structured to easily integrate the following advanced features in future iterations:
- **Jenkins CI/CD Pipeline Integration**: Automated execution triggered on pull requests and scheduled builds.
- **Parallel Test Execution**: Integration with `behave-parallel` or `pytest-xdist` to accelerate execution time.
- **Cross-Browser & Grid Testing**: Support for Firefox, Edge, and Selenium Grid / Cloud Services (Sauce Labs, BrowserStack).
- **Environment Configuration Management**: Multi-environment support (staging, QA, production) via configuration profiles.
- **Advanced Data-Driven Testing**: External test data management using JSON/CSV files.
- **API Testing Integration**: Hybrid testing combining REST API calls for setup/teardown with UI automation.

---

## Author

**Neha Shet**
- QA Automation Engineer
- Specializing in Python, Selenium WebDriver, BDD, and Framework Architecture.
