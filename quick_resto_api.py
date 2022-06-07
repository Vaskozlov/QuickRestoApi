import requests
import json
from requests.auth import HTTPBasicAuth


class QuickRestoApi:

    def __init__(self, login, password):
        self._login = login

    @property
    def login(self):
        return self._login
