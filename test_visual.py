from playwright.sync_api import Page

def test_nav_visual(page: Page, assert_snapshot):
    page.goto("https://www.monks.com/", wait_until="commit")
    nav = page.get_by_label("Primary navigation")
    nav.wait_for(state="visible")

    page.add_style_tag(content="""
        nav[aria-label="Primary navigation"] {
            background: #1a1a1a !important;
        }
    """)

    page.wait_for_timeout(2000)
    assert_snapshot(nav.screenshot(animations="disabled"), threshold=0.3)