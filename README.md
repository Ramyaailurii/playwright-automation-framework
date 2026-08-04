# Playwright Automation Framework

A Python + Playwright test automation framework built from scratch, covering Page Object Model design, real session authentication, API mocking, visual regression testing, parallel execution, and a full CI/CD pipeline on GitHub Actions.

Built as a self-directed learning project to transition from manual QA into test automation.

## What This Framework Demonstrates

- **Page Object Model** — locators and actions separated from test logic (`pages/monks_home_page.py`)
- **Session authentication caching** — real login flow with Playwright's `storage_state`, cutting per-test authenticated setup time from ~15s to under 5s (`create_auth_state.py`, `test_saved_auth.py`)
- **API mocking** — intercepting live network requests with `page.route()` and verifying the UI renders mocked data correctly (`test_api_mock.py`)
- **Visual regression testing** — pixel-level screenshot comparison against saved baselines, including handling animated backgrounds and cross-platform (macOS/Linux) rendering differences (`test_visual.py`)
- **Parallel test execution** — via `pytest-xdist`, distributing tests across multiple worker processes
- **CI/CD pipeline** — GitHub Actions workflow that runs the full suite on every push, with automatic failure artifacts (screenshots, video, Playwright trace files) and HTML reporting

## Tech Stack

Python 3.13 · Playwright · Pytest · pytest-xdist · pytest-html · pytest-playwright-visual · GitHub Actions

## Project Structure

```
├── .github/workflows/       # CI/CD pipeline (GitHub Actions)
├── pages/                   # Page Object classes
│   └── monks_home_page.py
├── snapshots/                # Visual regression baseline images
├── conftest.py               # Shared fixtures (homepage setup, browser context args)
├── create_auth_state.py      # Standalone script — logs in once, saves session to disk
├── test_navigation.py        # POM-based navigation test
├── test_api_mock.py          # API interception & mocking
├── test_visual.py            # Visual regression test
├── test_saved_auth.py        # Reuses saved auth session (storage_state)
├── pytest.ini                 # Parallel execution, reporting, and failure artifact config
└── requirements.txt
```

## Running the Tests Locally

```bash
pip install -r requirements.txt
playwright install --with-deps chromium
python3 create_auth_state.py     # generates a fresh authenticated session
pytest                            # runs the full suite in parallel
```

An HTML report is generated at `reports/execution_report.html` after every run.

## CI/CD

Every push to `main` automatically triggers the test suite via GitHub Actions:
- Fresh Ubuntu environment, dependencies installed from scratch
- Authenticated session regenerated per run
- Tests run in parallel across worker processes
- Screenshots, videos, and trace files captured automatically on failure and uploaded as build artifacts

## Real Debugging Notes

A few genuine issues hit and resolved while building this, worth knowing if extending the framework:

- **Cross-platform visual baselines:** `pytest-playwright-visual` names snapshot files by OS (`[darwin]` vs `[linux]`). A baseline captured locally on macOS won't match in Linux-based CI — CI needs its own generated baseline, retrieved via a build artifact and committed to the repo.
- **Headless CI timing:** a click that worked reliably in local runs occasionally failed in headless CI due to timing differences in when a dropdown's JavaScript finished attaching. Resolved with explicit `wait_for(state="visible")` calls rather than assuming immediate readiness.
- **`page.route()` scope:** it only intercepts requests made by the browser page itself (navigation, `fetch()` calls from page scripts) — it does not intercept Playwright's separate `page.request` API.

## Author

Ramya Ailuri — [LinkedIn](https://linkedin.com/in/ramya-ailuri-92106621b)