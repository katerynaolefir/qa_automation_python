import logging
import requests

class RequestUtils:

    logger = logging.getLogger('RequestUtils')

    def __init__(self):
        self.session = requests.Session()

    def send_request(self, method, path, params=None, json=None, auth=None,expected_status_code=None):

        self.logger.info(f'Sending {method} request to {path} with {params}')

        response = self.session.request(method, path, params=params, json=json, auth=auth, timeout=10)

        self.logger.info(f'Status code is: {response.status_code}')

        if expected_status_code is not None:
            assert response.status_code == expected_status_code, f'{method} {path} returns status code {response.status_code}, but should {expected_status_code}'

        return response