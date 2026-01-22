class LoginPage:
    URL = "https://the-internet.herokuapp.com/login"

    def __init__(self, page):
        self.page = page
        self.username_input = "#username"
        self.password_input = "#password"
        self.login_button = "button[type='submit']"
        self.success_message = ".flash.success"
        self.error_message = ".flash.error"

    def open(self):
        self.page.goto(self.URL)

    def login(self, username, password):
        self.page.fill(self.username_input, username)
        self.page.fill(self.password_input, password)
        self.page.click(self.login_button)

    def is_login_successful(self):
        return self.page.is_visible(self.success_message)

    def is_login_failed(self):
        return self.page.is_visible(self.error_message)
