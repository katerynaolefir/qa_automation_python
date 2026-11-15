from lesson_24._local_server.cars_app import cars_db

class CarAssertBase:

    def check_car_response_structure(self, car: dict):

        assert len(car['brand']) > 0
        assert car['year'] > 0
        assert car['engine_volume'] >= 0
        assert car['price'] > 0

    def check_cars_count(self, cars: list, limit: int):

        expected_count = min(limit, len(cars_db))
        assert len(cars) == expected_count, f'Expected {expected_count} cars, got {len(cars)}'

    def check_cars_is_sorted_by_parameter(self, cars: list, sort_by: str):

        sorted_list = sorted(cars, key=lambda car: car[sort_by])
        assert sorted_list == cars, f'List is not sorted by {sort_by}'

    def check_cars_match_expected(self, cars: list, sort_by: str, limit: int):

        expected_cars = sorted(cars_db.values(), key=lambda car: car[sort_by])[:limit]
        assert cars == expected_cars, f'Wrong cars for sort_by={sort_by}, limit={limit}'