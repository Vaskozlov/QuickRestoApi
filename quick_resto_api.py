import json

import requests
from requests.auth import HTTPBasicAuth


class QuickRestoApiException(BaseException):
    @property
    def message(self) -> str:
        return self._message

    @property
    def status(self) -> int:
        return self._status

    @property
    def response(self) -> requests.Response:
        return self._response

    def __init__(self, response: requests.Response):
        self._response: requests.Response = response
        self._status: int = response.status_code
        self._message: str = self._prettify_message()
        super().__init__(f"Http code is {self.status}.\nMessage from server:\n{self.message}")

    def _prettify_message(self) -> str:
        try:
            json_data = self.response.json()
            return json.dumps(json_data, sort_keys=True, ensure_ascii=False, indent=4)
        except requests.exceptions.JSONDecodeError:
            return self.response.text


class QuickRestoApi:
    @property
    def login(self) -> str:
        return self._login

    @property
    def base_url(self) -> str:
        return self._base_url

    @property
    def headers(self) -> dict:
        return self._headers

    def __init__(self, login: str, password: str, use_https: bool = True, layer: str = "quickresto.ru"):
        self._login: str = login
        self._password: str = password
        self._base_url: str = f'http{"s" * use_https}://{login}.{layer}/platform/online/'
        self._auth_data: HTTPBasicAuth = HTTPBasicAuth(self._login, self._password)
        self._headers: dict = {
            "Content-type": "application/json",
            "Connection": "keep-alive"
        }

    def post(self, url: str, parameters: dict = None, json_data: dict = None) -> requests.Response:
        response = requests.post(
            url=self.base_url + url,
            headers=self.headers,
            json=json_data,
            auth=self._auth_data,

            params=parameters
        )
        self._check_response(response)

        return response

    def get(self, url: str, parameters: dict = None, json_data: dict = None) -> requests.Response:
        response = requests.get(
            url=self.base_url + url,
            headers=self.headers,
            json=json_data,
            auth=self._auth_data,

            params=parameters
        )
        self._check_response(response)

        return response

    @staticmethod
    def _check_response(response: requests.Response) -> None:
        if response.status_code // 100 != 2:
            raise QuickRestoApiException(response)
