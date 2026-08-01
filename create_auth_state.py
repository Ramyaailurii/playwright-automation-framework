import os
from playwright.sync_api import sync_playwright

def create_auth_state():
    os.makedirs("playwright/.auth", exist_ok=True)

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(ignore_https_errors=True)
        page = context.new_page()

        page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        page.get_by_placeholder("Username").fill("Admin")
        page.get_by_placeholder("Password").fill("admin123")
        page.get_by_role("button", name="Login").click()
        page.wait_for_url("**/dashboard/index")

        context.storage_state(path="playwright/.auth/user.json")
        print("Auth state saved successfully.")

        browser.close()

create_auth_state()