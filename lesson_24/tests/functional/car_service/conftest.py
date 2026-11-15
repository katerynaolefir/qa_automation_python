import logging
import pytest
from lesson_24.core.api.cars_service.cars_controller import CarsController

logger = logging.getLogger(__name__)

@pytest.fixture(scope='class')
def authorized_cars_ctrl():
    logger.info('----------Get token------------')
    cars_ctrl = CarsController()

    token = cars_ctrl.get_token()['access_token']
    cars_ctrl.set_token(token)

    yield cars_ctrl

    logger.info('----------Session close------------')
    cars_ctrl.session.close()


@pytest.fixture
def cars_ctrl():
    cars_ctrl = CarsController()

    yield cars_ctrl

    cars_ctrl.session.close()