from src.check_search.webpage.helpers import check_search_webpage
from src.log.setup import setup_logger
from src.notifier.master import MasterNotifier


class WebpageChecker:

    def __init__(self, notifier: MasterNotifier):
        self.logger = setup_logger()
        self.notifier = notifier

    def check_webpage(self):
        print(f"Checking search webpage logic...")
        try:
            check_search_webpage()
        except Exception as e:
            msg = f"❌ Webpage check failed: {e}"
            self.logger.error(msg)
            self.notifier.notify(msg)
