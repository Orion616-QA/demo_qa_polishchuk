import configparser
import os
from pathlib import Path
from selenium.webdriver.chrome.webdriver import WebDriver as ChromeDriver
from selenium.webdriver.firefox.webdriver import WebDriver as FirefoxDriver
from selenium.webdriver.remote.webdriver import WebDriver as RemoteDriver

class Configuration:
    def __init__(self):
        # Всегда ищем config.ini в корне проекта
        project_root = Path(__file__).resolve().parent.parent
        config_path = project_root / "config.ini"

        self._parser = configparser.ConfigParser()
        read_files = self._parser.read(config_path)

        if not read_files:
            raise FileNotFoundError(f"❌ Config file not found at: {config_path}")

    def get_base_url(self):
        if not self._parser.has_section('demoqa'):
            raise RuntimeError("❌ Section [demoqa] not found in config.ini")
        return self._parser.get('demoqa', 'url')

    def get_browser(self):
        browser = self._get_driver()
        wait_time = self._parser.getfloat("browser", "wait")
        browser.implicitly_wait(wait_time)
        return browser

    @staticmethod
    def _get_driver():
        driver = os.getenv("BROWSER", "Chrome")
        if driver == "Chrome":
            return ChromeDriver()
        elif driver == "Firefox":
            return FirefoxDriver()
        else:
            return RemoteDriver()



CONFIG = Configuration()