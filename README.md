# Saauzi Whitelabel Test Automation Suite

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Selenium](https://img.shields.io/badge/Selenium-43B02A?style=for-the-badge&logo=Selenium&logoColor=white)
![Pytest](https://img.shields.io/badge/Pytest-0A9EDC?style=for-the-badge&logo=Pytest&logoColor=white)

A professional, robust, and scalable end-to-end test automation suite for the **Saauzi Whitelabel Partner Portal**. This project implements the **Page Object Model (POM)** design pattern to ensure maintainability, readability, and reliability of the automated tests.

---

## 🚀 Overview

This repository contains automated regression and functional tests for the [Saauzi Partner Portal](https://partner.saauzi.com/). The suite covers the entire user journey, from initial landing and registration to managing clients, subscriptions, and company profiles.

### Key Features
- **Page Object Model (POM):** Clean separation between page elements/actions and test logic.
- **Dynamic Data Generation:** Uses custom utility functions to generate random test data (emails, names, passwords) for exhaustive testing.
- **Negative & Security Testing:** Includes test cases for SQL injection, XSS, and invalid input validation.
- **CI/CD Ready:** Configured to run in headless mode for seamless integration with GitHub Actions or other CI pipelines.
- **Comprehensive Logging & Assertions:** Detailed test steps with robust assertions for every critical workflow.

---

## 🛠️ Tech Stack

- **Language:** Python 3.x
- **Framework:** Pytest
- **Automation Tool:** Selenium WebDriver
- **Design Pattern:** Page Object Model (POM)
- **Browser:** Google Chrome (Headless support included)

---

## 📂 Project Structure

```text
saauzi_whitelabel/
├── pages/                # Page Object Model implementations
│   ├── home.py           # Landing page actions
│   ├── signup.py         # Registration workflows
│   ├── login.py          # Authentication workflows
│   ├── dashboard.py      # Main dashboard interactions
│   ├── clients.py        # Client management
│   └── ...               # (Company Profile, Subscriptions, etc.)
├── tests/                # Test suite implementation
│   └── saauzi_whitelabel_test.py  # Master test file containing all scenarios
├── test_data/            # Utilities for generating dynamic test data
│   └── data.py           # Random generators and constants
├── conftest.py           # Pytest fixtures and browser setup
├── requirements.txt      # Project dependencies
└── README.md             # Project documentation
```

---

## 🔧 Installation & Setup

1. **Clone the Repository:**
   ```bash
   git clone <repository-url>
   cd saauzi_whitelabel
   ```

2. **Create a Virtual Environment:**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Linux/macOS
   .venv\Scripts\activate     # Windows
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Webdriver Setup:**
   Ensure you have the latest version of **Google Chrome** installed. The project uses `selenium` which automatically manages driver binaries in most modern versions, but ensure Chrome is in your PATH.

---

## 🧪 Running Tests

The test suite is highly modular and can be run in various configurations using `pytest`.

### Run All Tests
```bash
pytest tests/saauzi_whitelabel_test.py -v -s
```

### Run Specific Modules
- **Only Signup Tests:**
  ```bash
  pytest tests/saauzi_whitelabel_test.py -v -s -k "Signup"
  ```
- **Only Login Tests:**
  ```bash
  pytest tests/saauzi_whitelabel_test.py -v -s -k "Login"
  ```

### Run by Test Type
- **Positive Tests:**
  ```bash
  pytest tests/saauzi_whitelabel_test.py -v -s -k "positive"
  ```
- **Negative/Security Tests:**
  ```bash
  pytest tests/saauzi_whitelabel_test.py -v -s -k "negative"
  ```

---

## 📊 Test Coverage

The suite covers 9 major modules of the application:
1.  **Homepage:** Navigation links, CTAs, and layout verification.
2.  **Signup:** Positive registration, duplicate email handling, and input validation.
3.  **Login:** Successful authentication, session management, and error handling.
4.  **Dashboard:** Card visibility, summary statistics, and data filtering.
5.  **Clients:** End-to-end client creation and list verification.
6.  **Company Subscriptions:** Creating subscriptions, recording payments ($/₹), and status updates.
7.  **Client Logs:** Verification of audit trails and system logs.
8.  **Company Profile:** Dynamic updates of logos, favicons, and company metadata.
9.  **Purchase Plan:** Plan selection and navigation workflows.

---

## 🛡️ Security & Robustness
The suite specifically targets common vulnerabilities to ensure platform stability:
- **SQLi Probing:** Injects SQL payloads into authentication fields.
- **XSS Prevention:** Verifies that script payloads in company names are not executed.
- **Boundary Testing:** Tests with extremely long strings and special characters.

---

## 👤 Author
Developed and maintained as part of the Saauzi Whitelabel quality assurance initiative.
