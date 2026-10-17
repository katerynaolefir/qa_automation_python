import logging

import pytest

from lesson_24.core.api.cars_service.assertations.car_assertation import CarAssertBase
from lesson_24.data.search_params import SEARCH_PARAMS

logger = logging.getLogger(__name__)


class TestSearchCars:

    car_assert = CarAssertBase()

    @pytest.mark.parametrize('sort_by, limit', SEARCH_PARAMS)
    def test_search_cars(self, authorized_cars_ctrl, sort_by, limit):
        logger.info(f'Search cars sort_by={sort_by}, limit={limit}')

        cars = authorized_cars_ctrl.get_cars(query_parameters={'sort_by': sort_by, 'limit': limit})

        for car in cars:
            self.car_assert.check_car_response_structure(car)

        self.car_assert.check_cars_count(cars, limit)
        self.car_assert.check_cars_is_sorted_by_parameter(cars, sort_by)
        self.car_assert.check_cars_match_expected(cars, sort_by, limit)