import os

import dotenv
import requests
import json
import logging

from logging_logic import setup_logger
from constants import BASE_URL
from webhook_logic import DiscordPoster, SMSNotifier


def check_search_endpoint(webhook_url: str):
    discord_poster = DiscordPoster(webhook_url)
    sms_notifier = SMSNotifier()
    logger = setup_logger()
    try:
        response = requests.get(
            url=get_url(),
            params=get_search_query()
        )
        response.raise_for_status()  # Check for HTTP errors

        data = response.json()["data"]
        if len(data) > 0:
            logger.info("Search endpoint is functioning as expected.")
            msg = ("Testing SMS")
            sms_notifier.send_sms(msg)
        else:
            msg = "Search endpoint returned an empty response."
            logger.error(msg)
            discord_poster.post_to_discord(msg)
            sms_notifier.send_sms(msg)
    except Exception as e:
        msg = f"Search endpoint check failed: {e}"
        logger.error(msg)
        discord_poster.post_to_discord(msg)
        sms_notifier.send_sms(msg)


def get_url():
    url = f"{BASE_URL}/search-tokens"
    return url


def get_search_query():
    query = {
        "arg1": "stops",
        "arg2": "pittsburgh",
        "endpoint": "quick-search"
    }
    return query


if __name__ == "__main__":
    dotenv.load_dotenv()
    webhook_url = os.getenv("WEBHOOK_URL")
    check_search_endpoint(webhook_url)
