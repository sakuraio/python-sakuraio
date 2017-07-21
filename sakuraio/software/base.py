import requests
from sakuraio.software.apis import APIMixins


# Please check bottom of API docs.
API_VERSION = "1.0.3"


class SakuraIOClient(APIMixins):
    base_url = 'https://api.sakura.io/v1/'
    api_token = None
    api_secret = None

    def __init__(self, api_token, api_secret, base_url=None):
        if api_token is None or api_secret is None:
            Exception('[ERROR] must set api_token and api_secret')

        self.api_token = api_token
        self.api_secret = api_secret

        if base_url is not None:
            self.base_url = base_url

    def do(self, method, path, url_params={}, query_params={}, request_params={}):
        """Request wrapper

        :param string method:
            HTTP Mehod. ``GET`` or ``POST``.

        :param string path:
            Path of URL.

        :return: API response (format JSON)
        """
        headers = {}
        headers['Accept'] = 'application/json'
        auth = (self.api_token, self.api_secret)
        _url = self.base_url + path + '/'
        _url = _url.format(**url_params)

        method = method.lower()
        response = None
        if method == 'get':
            response = requests.get(
                _url,
                params=query_params,
                headers=headers,
                auth=auth
                )
        elif method == 'post':
            headers['Content-Type'] = 'application/json'
            response = requests.post(
                _url,
                params=query_params,
                json=request_params,
                headers=headers,
                auth=auth
                )
        elif method == 'delete':
            response = requests.delete(
                _url,
                headers=headers,
                auth=auth
                )
        elif method == 'put':
            response = requests.put(
                _url,
                params=query_params,
                json=request_params,
                headers=headers,
                auth=auth
                )
        else:
            raise Exception('[ERROR] Unsupported Method')

        if response.status_code >= 400:
            raise Exception(response, response.text)

        if response.status_code == 204:
            # 204 NO_CONTENT is blank response
            return None

        return response.json()

    def auth(self):
        """Test authentication
        """
        return self.do('GET', 'auth')
