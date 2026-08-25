# E-Commerce UI Automation Suite

Automated UI testing framework for the [SauceDemo / Swag Labs](https://www.saucedemo.com/) e-commerce web application.

## Tech Stack
- **Language**: Python 3.13
- **Automation Tool**: Selenium WebDriver
- **BDD Framework**: Behave
- **Design Pattern**: Page Object Model (POM)
- **Version Control**: Git

## Project Structure
```
ecommerce-ui-automation/
│
├── features/         # Gherkin feature files (.feature)
├── pages/            # Page Object Model classes
├── steps/            # Step definition implementations
├── utils/            # Driver factory and helper utilities
├── screenshots/      # Screenshots captured during test runs
├── reports/          # Test execution reports
├── requirements.txt  # Project dependencies
├── behave.ini        # Behave test runner configuration
├── README.md         # Project documentation
└── .gitignore        # Git ignore file
```

## Setup Instructions

### 1. Activate Virtual Environment
On Windows (PowerShell):
```powershell
.\venv\Scripts\Activate.ps1
```
On Windows (Command Prompt):
```cmd
.\venv\Scripts\activate.bat
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run Tests
```bash
behave
```
