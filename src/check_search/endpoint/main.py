from discord_poster import DiscordPoster
from environs import Env

from src.check_search.endpoint.check import check_search_endpoint
from src.notifier.master import MasterNotifier
from src.notifier.sms import SMSNotifier

if __name__ == "__main__":

    env = Env()
    env.read_env()
    webhook_url = env.str("WEBHOOK_URL")
    notifier_ = MasterNotifier(
        discord_poster=DiscordPoster(webhook_url),
        sms_notifier=SMSNotifier()
    )
    check_search_endpoint(notifier_)
