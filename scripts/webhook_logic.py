import logging
import os

import requests
import dotenv

class DiscordPoster:
    def __init__(self):
        dotenv.load_dotenv()
        self.webhook_url = os.getenv("WEBHOOK_URL")
        if not self.webhook_url:
            logging.error("WEBHOOK_URL environment variable not set")
            raise ValueError("WEBHOOK_URL environment variable not set")

    def post_to_discord(self, message):
        requests.post(self.webhook_url, json={"content": message})

def post_to_discord(message):
    dotenv.load_dotenv()
    webhook_url = os.getenv("WEBHOOK_URL")
    requests.post(webhook_url, json={"content": message})


if __name__ == "__main__":
    DiscordPoster().post_to_discord("Testing from health-monitoring")
