from playwright.sync_api import Page,expect

class MonksHomePage():
    def __init__(self,page:Page):
        self.page = page
        self.url = "https://www.monks.com/"
        self.accept_cookies_btn = page.get_by_role("button", name="Accept all")
        self.solutions_link = page.get_by_label("Primary navigation").get_by_text("Solutions")
        self.real_time_brands_link = page.get_by_role("link", name="Real-Time Brands", exact=True)

    def navigate(self):
        self.page.goto(self.url,wait_until="commit")
    def cookie_handle_banner(self):
        if self.accept_cookies_btn.is_visible():
            self.accept_cookies_btn.click()
    def click_solutions(self):
        self.solutions_link.click()
    def click_real_time_brands(self):
        self.real_time_brands_link.wait_for(state="visible")
        self.real_time_brands_link.click()