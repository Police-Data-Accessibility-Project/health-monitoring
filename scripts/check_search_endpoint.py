import requests
import json

from scripts.constants import BASE_URL

def check_search_endpoint():
    url = f"{BASE_URL}/search-tokens"
    query = {
        "arg1": "stops",
        "arg2": "pittsburgh",
        "endpoint": "quick-search"
    }

    try:
        response = requests.get(url, params=query)
        response.raise_for_status()  # Check for HTTP errors

        data = response.json()["data"]
        if len(data) > 0:
            print("Search endpoint is functioning as expected.")
        else:
            print("Search endpoint returned unexpected results.")
            # Trigger an alert or log the issue
    except requests.RequestException as e:
        print(f"Search endpoint check failed: {e}")
        # Trigger an alert or log the issue

if __name__ == "__main__":
    check_search_endpoint()
    # reset_password("maxachis@gmail.com")
    # create_user("maxachis@gmail.com", "BaklavaBoysBurnishingBrocolli")