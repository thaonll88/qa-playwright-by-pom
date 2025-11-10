from playwright.sync_api import expect
from config import settings

def test_valid_login_redirects(page, login_page, inventory_page):
    # Open login
    login_page.goto(settings.BASE_URL)
    # Do login
    login_page.login(settings.VALID_USERNAME, settings.VALID_PASSWORD)
    # Verify redirect
    inventory_page.assert_loaded()

def test_invalid_login_shows_error(page, login_page):
    login_page.goto(settings.BASE_URL)
    login_page.login(settings.INVALID_USERNAME, settings.INVALID_PASSWORD)

    # stay at login page & error banner
    expect(page).to_have_url(settings.BASE_URL)
    assert "Epic sadface" in login_page.error_text()

def test_locked_user_shows_specific_error(page, login_page):
    login_page.goto(settings.BASE_URL)
    login_page.login(settings.LOCKED_USERNAME, settings.VALID_PASSWORD)

    # Locked user message
    msg = login_page.error_text()
    assert "locked out" in msg.lower()
