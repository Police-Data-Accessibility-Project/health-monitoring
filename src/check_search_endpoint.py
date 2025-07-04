import os

import dotenv
import requests

from constants import BASE_URL
from notifier import MasterNotifier
from webhook_logic import DiscordPoster, SMSNotifier

ENDPOINT_NAME = "Typeahead"

def check_search_endpoint(notifier: MasterNotifier):
    print(f"Checking {ENDPOINT_NAME} endpoint...")
    try:
        response = requests.get(
            url=get_url(),
        )
        response.raise_for_status()  # Check for HTTP errors
        data = response.json()["suggestions"]
        evaluate_response(data, notifier)
    except Exception as e:
        msg = f"{ENDPOINT_NAME} endpoint check failed: {e}"
        notifier.notify(msg)


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
    notifier = MasterNotifier(
        discord_poster=DiscordPoster(webhook_url),
        sms_notifier=SMSNotifier()
    )
    check_search_endpoint(notifier)
