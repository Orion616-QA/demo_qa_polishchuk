import requests
from configuration import CONFIG

def test_smoke():
    response = requests.get(CONFIG.get_base_url())
    response.raise_for_status()