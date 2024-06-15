import logging
import os

import requests
import dotenv

class DiscordPoster:
    def __init__(self, webhook_url: str):
        dotenv.load_dotenv()
        if not webhook_url:
            logging.error("WEBHOOK_URL environment variable not set")
            raise ValueError("WEBHOOK_URL environment variable not set")
        self.webhook_url = webhook_url
    def post_to_discord(self, message):
        requests.post(self.webhook_url, json={"content": message})

if __name__ == "__main__":
    DiscordPoster().post_to_discord("Testing from health-monitoring")
