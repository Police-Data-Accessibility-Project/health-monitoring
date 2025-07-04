from discord_poster import DiscordPoster

from src.log.setup import setup_logger
from src.notifier.sms import SMSNotifier


class MasterNotifier:
    def __init__(
            self,
            discord_poster: DiscordPoster,
            sms_notifier: SMSNotifier
    ):
        self.logger = setup_logger()
        self.discord_poster = discord_poster
        self.sms_notifier = sms_notifier

    def notify(self, msg: str):
        print(msg)
        self.logger.info(msg)
        self.discord_poster.post_to_discord(msg)
        self.sms_notifier.send_sms(msg)

    def info(self, msg: str):
        self.logger.info(msg)
