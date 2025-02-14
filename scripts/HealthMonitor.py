import os

import dotenv

from scripts.Notifier import MasterNotifier
from scripts.check_search_endpoint import check_search_endpoint
from scripts.check_search_webpage import WebpageChecker
from scripts.webhook_logic import DiscordPoster, SMSNotifier


class HealthMonitor:

    def __init__(
            self,
            notifier: MasterNotifier
    ):
        self.notifier = notifier
        self.webpage_checker = WebpageChecker(notifier)

    def run(self):
        self.webpage_checker.check_webpage()
        check_search_endpoint(self.notifier)


if __name__ == "__main__":
    dotenv.load_dotenv()
    webhook_url = os.getenv("WEBHOOK_URL")
    notifier = MasterNotifier(
        discord_poster=DiscordPoster(webhook_url),
        sms_notifier=SMSNotifier()
    )
    hm = HealthMonitor(notifier)
    hm.run()