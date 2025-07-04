import requests

from src.check_search.endpoint.constants import ENDPOINT_NAME, BASE_URL
from src.notifier.master import MasterNotifier


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


def evaluate_response(data: list, notifier: MasterNotifier):
    if len(data) > 0:
        notifier.info(f"{ENDPOINT_NAME} endpoint is functioning as expected.")
    else:
        msg = f"{ENDPOINT_NAME} endpoint returned an empty response."
        notifier.notify(msg)


def get_url():
    url = f"{BASE_URL}/typeahead/locations?query=Pitt"
    return url


