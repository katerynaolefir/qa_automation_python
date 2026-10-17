import logging
import pytest

logger = logging.getLogger(__name__)


class TestSearchCarsNegative:

    def test_search_without_token(self, cars_ctrl):
        logger.info('Search cars without token')

        response = cars_ctrl.get_cars(
            query_parameters={'sort_by': 'price', 'limit': 3},
            expected_status_code=401
        )

        assert response['msg'] == 'Missing Authorization Header'

    @pytest.mark.parametrize('username, password', [
        ('test_user', 'wrong_pass'),
        ('wrong_user', 'test_pass'),
    ])
    def test_auth_with_wrong_creds(self, cars_ctrl, username, password):
        logger.info(f'Auth with username={username}, wrong creds')

        response = cars_ctrl.get_token(username, password,expected_status_code=401)

        assert 'access_token' not in response