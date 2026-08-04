import pytest
from playwright.sync_api import Page, expect

def test_mock_time_at_work(page: Page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    page.get_by_placeholder("Username").fill("Admin")
    page.get_by_placeholder("Password").fill("admin123")
    page.get_by_role("button", name="Login").click()
    page.wait_for_url("**/dashboard/index")

    mock_response = {
        "data": [
            {"workDay": {"id": "1", "day": "Mon", "date": "2026-07-27"}, "totalTime": {"hours": 0, "minutes": 0}},
            {"workDay": {"id": "2", "day": "Tue", "date": "2026-07-28"}, "totalTime": {"hours": 0, "minutes": 0}},
            {"workDay": {"id": "3", "day": "Wed", "date": "2026-07-29"}, "totalTime": {"hours": 0, "minutes": 0}},
            {"workDay": {"id": "4", "day": "Thu", "date": "2026-07-30"}, "totalTime": {"hours": 0, "minutes": 0}},
            {"workDay": {"id": "5", "day": "Fri", "date": "2026-07-31"}, "totalTime": {"hours": 3, "minutes": 8}},
            {"workDay": {"id": "6", "day": "Sat", "date": "2026-08-01"}, "totalTime": {"hours": 0, "minutes": 0}},
            {"workDay": {"id": "0", "day": "Sun", "date": "2026-08-02"}, "totalTime": {"hours": 0, "minutes": 0}}
        ],
        "meta": {
            "lastAction": {
                "state": "PUNCHED OUT", "utcDate": "2026-07-31", "utcTime": "07:09",
                "userDate": "2026-07-31", "userTime": "12:39", "timezoneOffset": "5.5"
            },
            "currentDay": {
                "currentDate": {"date": "2026-07-28", "label": "Jul 28"},
                "totalTime": {"hours": 8, "minutes": 45}
            },
            "currentWeek": {
                "startDate": {"date": "2026-07-27", "label": "Jul 27"},
                "endDate": {"date": "2026-08-02", "label": "Aug 02"},
                "totalTime": {"hours": 3, "minutes": 8}
            },
            "currentUser": {
                "empNumber": 7, "firstName": "John", "middleName": "Shree",
                "lastName": "India", "terminationId": None
            }
        },
        "rels": []
    }

    def log_and_mock(route):
        route.fulfill(
            status=200,
            content_type="application/json",
            json=mock_response
        )

    page.route("**/api/v2/dashboard/employees/time-at-work*", log_and_mock)
    page.reload()

    expect(page.get_by_text("8h 45m")).to_be_visible()