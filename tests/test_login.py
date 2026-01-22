from pages.login_page import LoginPage

def test_login_success(page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login("tomsmith", "SuperSecretPassword!")
    assert login_page.is_login_successful()

def test_login_invalid_password(page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login("tomsmith", "wrongpassword")
    assert login_page.is_login_failed()
