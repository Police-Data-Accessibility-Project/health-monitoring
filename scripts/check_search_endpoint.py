import requests
import json

from constants import BASE_URL
from webhook_logic import post_to_discord

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
            print("HEALTH_MONITORING: Search endpoint is functioning as expected.")
        else:
            post_to_discord("Search endpoint returned unexpected results.")
    except requests.RequestException as e:
        post_to_discord(f"Search endpoint check failed: {e}")

if __name__ == "__main__":
    check_search_endpoint()
