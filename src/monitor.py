from src.notifier.master import MasterNotifier
from src.check_search.endpoint.check import check_search_endpoint
from src.check_search.webpage.checker import WebpageChecker


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

