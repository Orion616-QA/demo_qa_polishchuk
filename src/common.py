from abc import ABC

from configuration import CONFIG

class BasePage(ABC):
    def __init__(self, driver):
        self._driver = driver

    def open(self):
        self._driver.get(CONFIG.BASE_URL)