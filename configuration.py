import configparser
import os

config_parser = configparser.ConfigParser()
config_parser.read("config.ini")

class Configuration:
    def __init__(self):
        self._parser = configparser.ConfigParser()
        self._parser.read(os.getenv('CONFIG_PATH', 'config.ini'))

    def get_browser(self):
        pass
    # TODO DEMO-QA-003 Implementing getting selenium driver in config class