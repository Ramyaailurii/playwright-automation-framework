from playwright.sync_api import Page , expect
from pages.monks_home_page import MonksHomePage

def test_click_solutions(monks_homepage):
    monks_homepage.click_solutions()
    monks_homepage.click_real_time_brands()
    print(monks_homepage.page.url)
    expect(monks_homepage.page).to_have_url("https://www.monks.com/solutions/real-time-brands")