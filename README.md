# QA Automation with Playwright (Python)

This project is a basic **QA automation framework** built with **Python, pytest, and Playwright**.
It demonstrates automated UI testing using the **Page Object Model (POM)** pattern.

The project is designed as a **junior QA automation portfolio project**, focusing on clarity, structure, and correctness.

---

##  What Is Tested
- Login functionality
- Successful login with valid credentials
- Error handling with invalid credentials

Test site used:
https://the-internet.herokuapp.com/login

---

## Tech Stack
- Python
- pytest
- Playwright
- Page Object Model (POM)

---

## Project Structure
qa-automation-playwright/
├── pages/ # Page Objects
├── tests/ # Test cases
├── screenshots/ # Screenshots from test execution
├── reports/ # Test execution reports
├── conftest.py # pytest fixtures
├── pytest.ini # pytest configuration
├── requirements.txt
└── README.md

---


##  How to Run the Tests

### 1️⃣ Create and activate virtual environment

        python -m venv .venv
        source .venv/bin/activate

    2️⃣ Install dependencies

        pip install -r requirements.txt
        playwright install

    3️⃣ Run tests

        pytest

---

✅ Project Status
The project is actively being improved.
New features are added incrementally following real-world QA automation practices.

---

👤 Author
QA Automation portfolio project using Python and Playwright.