import requests
import dotenv


def post_to_discord(message):
    dotenv.load_dotenv()
    webhook_url = os.getenv("WEBHOOK_URL")
    requests.post(webhook_url, json={"content": message})


if __name__ == "__main__":
    post_to_discord("Testing from health-monitoring")