from discord_poster import DiscordPoster
from environs import Env

from src.check_search.webpage.checker import WebpageChecker
from src.notifier.master import MasterNotifier
from src.notifier.sms import SMSNotifier

if __name__ == "__main__":
    env = Env()
    env.read_env()
    webhook_url = env.str("WEBHOOK_URL")
    notifier = MasterNotifier(
        discord_poster=DiscordPoster(webhook_url),
        sms_notifier=SMSNotifier()
    )
    wc = WebpageChecker(notifier)
    wc.check_webpage()