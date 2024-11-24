import os

import dotenv
import requests
import json
import logging

from logging_logic import setup_logger
from constants import BASE_URL
from webhook_logic import DiscordPoster, SMSNotifier

ENDPOINT_NAME = "Typeahead"

class Notifier:
    def __init__(self, webhook_url: str, notify=True):
        self.webhook_url = webhook_url
        self.logger = setup_logger()
        self.notify = notify

    def handle_error(self, msg: str):
        self.logger.error(msg)
        if self.notify:
            DiscordPoster(self.webhook_url).post_to_discord(msg)
            SMSNotifier().send_sms(msg)

    def info(self, msg: str):
        self.logger.info(msg)


def check_search_endpoint(webhook_url: str, notify=True):
    notifier = Notifier(webhook_url=webhook_url, notify=notify)
    try:
        response = requests.get(
            url=get_url(),
        )
        response.raise_for_status()  # Check for HTTP errors
        data = response.json()["suggestions"]
        evaluate_response(data, notifier)
    except Exception as e:
        msg = f"{ENDPOINT_NAME} endpoint check failed: {e}"
        notifier.handle_error(msg)


def evaluate_response(data, notifier):
    if len(data) > 0:
        notifier.info(f"{ENDPOINT_NAME} endpoint is functioning as expected.")
    else:
        msg = f"{ENDPOINT_NAME} endpoint returned an empty response."
        notifier.handle_error(msg)


def get_url():
    url = f"{BASE_URL}/typeahead/locations?query=Pitt"
    return url



if __name__ == "__main__":
    dotenv.load_dotenv()
    webhook_url = os.getenv("WEBHOOK_URL")
    check_search_endpoint(webhook_url, notify=False)
