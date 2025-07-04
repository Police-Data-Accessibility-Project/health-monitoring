from discord_poster import DiscordPoster
from environs import Env

from src.monitor import HealthMonitor
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
    hm = HealthMonitor(notifier)
    hm.run()