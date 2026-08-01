from playwright.sync_api import Page, expect
def test_nav_visual(page: Page, assert_snapshot):
    page.goto("https://www.monks.com/", wait_until="commit")
    nav = page.get_by_label("Primary navigation")
    nav.wait_for(state="visible")

    page.add_style_tag(content="""
        nav[aria-label="Primary navigation"] {
            background: #1a1a1a !important;
        }
    """)

    page.wait_for_timeout(2000)  # longer wait — give the stagger animation time to fully finish
    assert_snapshot(nav.screenshot(animations="disabled"))  # also force-disable any remaining CSS animation