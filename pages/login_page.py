from playwright.sync_api import Page, Locator

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username_input: Locator = page.get_by_placeholder("Username")
        self.password_input: Locator = page.get_by_placeholder("Password")
        self.login_button: Locator   = page.get_by_role("button", name="Login")
        self.error_banner: Locator   = page.locator("[data-test='error']")

    def goto(self, base_url: str):
        self.page.goto(base_url)

    def login(self, username: str, password: str):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def error_text(self) -> str:
        if self.error_banner.is_visible():
            return self.error_banner.inner_text()
        return ""
