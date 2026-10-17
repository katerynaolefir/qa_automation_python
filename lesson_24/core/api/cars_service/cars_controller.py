import requests
from requests.auth import HTTPBasicAuth

from lesson_24.utils.request_utils import RequestUtils


class CarsController(RequestUtils):

    def __init__(self, base_url='http://127.0.0.1:8080'):
        self.base_url = base_url
        self.session = requests.Session()

    def get_token(self,
                  username='test_user', 
                  password='test_pass',
                  expected_status_code=200):
        response = self.send_request(
            method='POST', path=f'{self.base_url}/auth',
            auth=HTTPBasicAuth(username, password),
            expected_status_code=expected_status_code)

        return response.json()

    def set_token(self, access_token):
        self.session.headers.update({'Authorization': 'Bearer ' + access_token})

    def get_cars(self, query_parameters=None, expected_status_code=200):
        response = self.send_request(
            method='GET', path=f'{self.base_url}/cars',
            params=query_parameters, expected_status_code=expected_status_code)

        return response.json()