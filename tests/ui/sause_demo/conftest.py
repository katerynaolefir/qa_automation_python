import pytest
from playwright.sync_api import sync_playwright, expect


@pytest.fixture(scope='session')

def home_page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)

        yield browser
        browser.close()
