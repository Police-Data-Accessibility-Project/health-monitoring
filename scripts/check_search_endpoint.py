import requests
import json
import logging

from logging_logic import setup_logger
from constants import BASE_URL
from webhook_logic import post_to_discord


def check_search_endpoint():
    url = f"{BASE_URL}/search-tokens"
    query = {
        "arg1": "stops",
        "arg2": "pittsburgh",
        "endpoint": "quick-search"
    }

    logger = setup_logger()
    try:
        response = requests.get(url, params=query)
        response.raise_for_status()  # Check for HTTP errors

        data = response.json()["data"]
        if len(data) > 0:
            logger.info("Search endpoint is functioning as expected.")
        else:
            msg = "Search endpoint returned an empty response."
            logger.error(msg)
            post_to_discord(msg)
    except Exception as e:
        msg = f"Search endpoint check failed: {e}"
        logger.error(msg)
        post_to_discord(msg)


if __name__ == "__main__":
    check_search_endpoint()
