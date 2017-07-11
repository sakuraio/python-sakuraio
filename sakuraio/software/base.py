import requests


class SakuraIOClient(object):
    base_url = 'https://api.sakura.io/'
    api_token = None
    api_secret = None

    def __init__(self, api_token, api_secret, base_url=None):
        if api_token is None or api_secret is None:
            Exception('[ERROR] must set api_token and api_secret')

        self.api_token = api_token
        self.api_secret = api_secret

        if base_url is not None:
            self.base_url = base_url

    def do(self, method, url, url_params={}, query_params={}, request_params={}):
        headers = {}
        headers["authorization"] = "Basic " + (self.api_token + ":" + self.api_secret).encode("base64")[:-1]
        headers["Accept"] = 'application/json'
        url = url.lstrip('/')
        _url = self.base_url + url

        method = method.lower()
        response = None
        if method == 'get':
            response = requests.get(_url, params=query_params)

        return response.json()
