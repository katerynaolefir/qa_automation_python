import pytest
from assertpy import soft_assertions, assert_that
from data_for_test import car_data_filtered


@pytest.mark.parametrize("search_criteria", [
    (2017, 1.6, 36000),
    (2018, 2.0, 50000),
    (2021, 1.4, 30000),
])
def test_found_cars_match_criteria(search_criteria):
    year_min, engine_volume_min, price_max = search_criteria
    result = car_data_filtered.find_cars(car_data_filtered.car_data, search_criteria)

    with soft_assertions():
        for car in result:
            price, name, color, year, engine_volume, car_type = car
            assert_that(year).is_greater_than_or_equal_to(year_min)
            assert_that(engine_volume).is_greater_than_or_equal_to(engine_volume_min)
            assert_that(price).is_less_than_or_equal_to(price_max)


def test_sorted_by_price():
    result = car_data_filtered.find_cars(car_data_filtered.car_data, (2016, 1.0, 2000000))
    prices = [car[0] for car in result]
    assert_that(prices).is_equal_to(sorted(prices))


def test_max_five_results():
    result = car_data_filtered.find_cars(car_data_filtered.car_data, (2016, 0.0, 2000000))
    assert_that(len(result)).is_less_than_or_equal_to(5)


def test_no_matches_returns_empty_list():
    result = car_data_filtered.find_cars(car_data_filtered.car_data, (2025, 10.0, 1000))
    assert_that(result).is_empty()


def test_not_empty_for_normal_criteria():
    result = car_data_filtered.find_cars(car_data_filtered.car_data, (2017, 1.6, 36000))
    assert_that(len(result)).is_greater_than(0)


@pytest.mark.parametrize("name, info", car_data_filtered.car_data.items())
def test_car_data_is_valid(name, info):
    color, year, engine_volume, car_type, price = info

    with soft_assertions():
        assert_that(price).is_greater_than(0)
        assert_that(year).is_greater_than(1900)
        assert_that(engine_volume).is_greater_than_or_equal_to(0)
        assert_that(color).is_not_empty()
        assert_that(car_type).is_not_empty()