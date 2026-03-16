# QA Automation Framework (Playwright)

## Description

This project demonstrates automated UI testing using Playwright with Python.

The framework is built to practice end-to-end browser automation and structured test organization.
It uses the Page Object Model (POM) pattern to separate test logic from page interactions and make tests easier to maintain.

The goal of the project is to demonstrate the basics of QA automation and browser testing.

---

## Running the Tests

Clone the repository.

Create a virtual environment.

Install dependencies:

```
pip install -r requirements.txt
```

Install Playwright browsers:

```
playwright install
```

Run all tests:

```
pytest
```

Run a specific test file:

```
pytest tests/test_login.py
```

---

## Technology Stack

* Python
* Playwright
* Pytest
* Page Object Model (POM)
* Git

---

## Framework Structure

```
QA-AUTOMATION-PLAYWRIGHT
│
├── pages
│   └── page_objects.py
│
├── tests
│   └── test_example.py
│
├── conftest.py
│
└── README.md
```

### Folder Overview

**pages/**
Contains page objects that store locators and page actions.

**tests/**
Contains automated test cases.

**conftest.py**
Provides shared fixtures used by tests.

---

## Design Diagram

The automation framework follows this structure:

```
Test Cases
   │
   ▼
Page Objects
   │
   ▼
Playwright API
   │
   ▼
Browser (Chromium / Firefox / WebKit)
```

Tests call methods from the page objects, which interact with the browser using Playwright.

---


## Purpose

This project was created as part of learning QA automation with Python and Playwright.

The focus of the project is to practice browser automation, structured test organization, and basic test framework design.
