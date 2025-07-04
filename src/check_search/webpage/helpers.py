from playwright.sync_api import sync_playwright

from src.check_search.webpage.constants import URL, NETWORK_IDLE, TIMEOUT_MILLISECONDS
from src.check_search.webpage.exceptions import CheckWebpageError


def check_search_webpage():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        page = browser.new_page()
        try:
            check_search_webpage_inner_logic(page)
            print("🎉 Test completed successfully!")
        except Exception as e:
            raise CheckWebpageError(f"❌ Test failed: {e}")
        finally:
            browser.close()

def navigate_to_page(page):
    try:
        page.goto(URL)
        page.wait_for_load_state(NETWORK_IDLE, timeout=TIMEOUT_MILLISECONDS)
        print("✅ Successfully loaded the webpage.")
    except Exception as e:
        raise CheckWebpageError(f"❌ Failed to load webpage '{URL}': {e}")

def fill_search_box(page):
    try:
        page.fill('input[id="pdap-search-typeahead"]', 'Pittsburgh')
        page.wait_for_load_state(NETWORK_IDLE, timeout=TIMEOUT_MILLISECONDS)
        print("✅ Successfully filled the search box.")
    except Exception as e:
        raise CheckWebpageError(f"❌ Failed to fill the search box: {e}")

def select_allegheny_pa(page):
    text = 'Allegheny, Pennsylvania'
    try:
        page.wait_for_selector('.pdap-typeahead-list')
        page.click(f'.pdap-typeahead-list-item:has-text("{text}")')
        print(f"✅ Successfully selected '{text}'.")
    except Exception as e:
        raise CheckWebpageError(f"❌ Failed to select '{text}': {e}")

def click_search_button(page):
    try:
        page.click('button:has-text("Search")')
        page.wait_for_load_state(NETWORK_IDLE, timeout=TIMEOUT_MILLISECONDS)
        print("✅ Successfully clicked Search button.")
    except Exception as e:
        raise CheckWebpageError(f"❌ Failed to click Search button: {e}")

def navigate_to_crime_statistics(page):
    try:
        page.wait_for_selector('a.agency-row.group:has-text("Crime Statistics for Swissvale")')
        page.click('a.agency-row.group:has-text("Crime Statistics for Swissvale")')
        print("✅ Successfully navigated to Crime Statistics for Swissvale.")
    except Exception as e:
        raise CheckWebpageError(f"❌ Failed to navigate to Crime Statistics for Swissvale: {e}")

def confirm_crime_statistics_page(page):
    try:
        page.wait_for_selector('h1:has-text("Crime Statistics for Swissvale")')
        print("✅ Successfully confirmed Crime Statistics for Swissvale page.")
    except Exception as e:
        raise CheckWebpageError(f"❌ Failed to confirm Crime Statistics for Swissvale page: {e}")

def click_next(page):
    try:
        page.click('a:has-text("NEXT")')
        page.wait_for_load_state(NETWORK_IDLE, timeout=TIMEOUT_MILLISECONDS)
        print("✅ Successfully clicked NEXT.")
    except Exception as e:
        raise CheckWebpageError(f"❌ Failed to click NEXT: {e}")

def confirm_record_request_info_page(page):
    try:
        page.wait_for_selector('h1:has-text("Record Request Info Swissvale Borough")')
        print("✅ Successfully confirmed Record Request Info Swissvale Borough page.")
    except Exception as e:
        raise CheckWebpageError(f"❌ Failed to confirm Record Request Info Swissvale Borough page: {e}")


def check_search_webpage_inner_logic(page):
    navigate_to_page(page)
    fill_search_box(page)
    select_allegheny_pa(page)
    click_search_button(page)
    navigate_to_crime_statistics(page)
    confirm_crime_statistics_page(page)
    click_next(page)
    confirm_record_request_info_page(page)



