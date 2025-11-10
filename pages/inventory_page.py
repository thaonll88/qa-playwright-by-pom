import re
from playwright.sync_api import Page, Locator, expect

class InventoryPage:
    def __init__(self, page: Page):
        self.page = page
        self.title: Locator = page.locator(".title")

    def assert_loaded(self):
        # correct URL + title visible
        expect(self.page).to_have_url(re.compile(r".*inventory\.html"))
        expect(self.title).to_be_visible()
        expect(self.title).to_have_text("Products")