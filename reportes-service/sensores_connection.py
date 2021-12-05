import requests
import os

class SensoresConnection():
    def __init__(self):
        self.url = str(os.getenv("SENSORES_SERVICE_URL"))

    def get_info(self):
        r = requests.get(self.url)
        return r.json()
