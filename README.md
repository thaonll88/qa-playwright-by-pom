# Playwright (Python) – Login E2E with POM

## Tech Stack
- Python 3.12+
- pytest
- pytest-playwright
- playwright
- Pattern: Page Object Model (POM)
- CI: GitHub Actions
- Report: pytest-html

## Folder Structure
pages/                # POM classes
  login_page.py
  inventory_page.py
tests/
  test_login_pom.py   # tests using POM
config/
  settings.py         # base URL & credentials
conftest.py           # pytest fixtures for POM
requirements.txt
.github/workflows/tests.yml
README.md

## Setup (local)
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
python -m playwright install

## Run tests
# Headless (CI mode)
pytest -q

# Headed (see browser)
pytest -q --headed

# With report, trace, video, screenshots
pytest -q --html=report.html --self-contained-html \
  --tracing=retain-on-failure --video=on --screenshot=only-on-failure

## Open Playwright Trace Viewer (after failure)
playwright show-trace test-results/**/trace.zip

## Test Scenarios
✅ Valid login → redirect to inventory page
✅ Invalid login → error banner visible
✅ Locked user → specific “user locked” message

## CI (GitHub Actions)
Workflow: .github/workflows/tests.yml
Artifacts uploaded:
- report.html
- test-results/ (trace, video, screenshot)