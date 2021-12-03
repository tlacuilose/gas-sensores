import requests

class SensoresConnection():
    def __init__(self, url):
        self.url = url

    def get_info(self):
        r = requests.get(self.url)
        return r.json()
