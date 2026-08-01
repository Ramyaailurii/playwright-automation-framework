# conftest.py
import pytest
from playwright.sync_api import Page
from pages.monks_home_page import MonksHomePage

@pytest.fixture
def monks_homepage(page: Page):
    homepage = MonksHomePage(page)
    homepage.navigate()
    homepage.cookie_handle_banner()
    return homepage
@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "ignore_https_errors": True,
    }