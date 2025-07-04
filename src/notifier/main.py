from discord_poster import DiscordPoster
from environs import Env

from src.notifier.master import MasterNotifier
from src.notifier.sms import SMSNotifier

if __name__ == "__main__":
    env = Env()
    env.read_env()

    notifier = MasterNotifier(
        discord_poster=DiscordPoster(env.str("WEBHOOK_URL")),
        sms_notifier=SMSNotifier()
    )
    notifier.notify("Testing notification from health-monitoring")
