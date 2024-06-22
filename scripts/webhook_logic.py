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

class SMSNotifier:
    def __init__(self):
        dotenv.load_dotenv()
        self.textbelt_api_url = os.getenv('TEXTBELT_API_URL', 'https://textbelt.com/text')
        self.textbelt_api_key = os.getenv('TEXTBELT_API_KEY')
        self.to_phone_number = os.getenv('SMS_NUMBER')

        if not self.textbelt_api_key or not self.to_phone_number:
            logging.error("SMS API credentials or recipient phone number not set in environment variables")
            raise ValueError("SMS API credentials or recipient phone number not set in environment variables")

    def send_sms(self, message):
        data = {
            'phone': self.to_phone_number,
            'message': message,
            'key': self.textbelt_api_key,
            'sender': 'Police Data Accessibility Project'
        }
        response = requests.post(self.textbelt_api_url, data=data)
        logging.info(f'SMS sent with response: {response.json()}')
        return response

if __name__ == "__main__":
    DiscordPoster().post_to_discord("Testing Discord post from health-monitoring")

    SMSNotifier().send_sms("Testing SMS rom health-monitoring")
    
