from abc import ABC, abstractmethod


class Scraper(ABC):
    """Uses product supplier row info
    to try to find live data"""

    @abstractmethod
    def lookup_product(ps):
        pass
