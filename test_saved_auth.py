from playwright.sync_api import Page, expect

def test_dashboard_with_saved_auth(browser):
    context = browser.new_context(storage_state="playwright/.auth/user.json")
    page = context.new_page()
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")
    expect(page).to_have_url("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")
    context.close()