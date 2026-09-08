import pytest
from assertpy import assert_that
from data_for_test import simple_functions


@pytest.mark.parametrize("a, b, expected", [
    (10, 14, 24),
    (0, 0, 0),
    (-5, 5, 0),
    (-3, -7, -10),
])
def test_sum_of_numbers(a, b, expected):
    assert_that(simple_functions.sum_of_numbers(a, b)).is_equal_to(expected)

def test_sum_of_numbers_is_positive():
    assert_that(simple_functions.sum_of_numbers(5, 10)).is_greater_than(0)

def test_sum_of_numbers_type_is_int():
    assert_that(simple_functions.sum_of_numbers(2, 3)).is_instance_of(int)



@pytest.mark.parametrize("numbers, expected", [
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5.5),
    ([2, 4, 6], 4),
    ([5], 5),
])
def test_average(numbers, expected):
    assert_that(simple_functions.average(numbers)).is_equal_to(expected)

def test_average_is_between_min_and_max():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = simple_functions.average(numbers)
    assert_that(result).is_greater_than_or_equal_to(min(numbers))
    assert_that(result).is_less_than_or_equal_to(max(numbers))


@pytest.mark.parametrize("text, expected", [
    ("hello", "olleh"),
    ("Python", "nohtyP"),
    ("", ""),
])
def test_reversed_string(text, expected):
    assert_that(simple_functions.reversed_string(text)).is_equal_to(expected)

def test_reversed_string_same_length():
    text = "Python"
    result = simple_functions.reversed_string(text)
    assert_that(result).is_length(len(text))


def test_reversed_string_contains_same_letters():
    text = "abc"
    result = simple_functions.reversed_string(text)
    assert_that(result).contains("a", "b", "c")


@pytest.mark.parametrize("words, expected", [
    (["Функція", "яка", "приймаєє", "список", "слів"], "приймаєє"),
    (["a", "bb", "ccc"], "ccc"),
])
def test_the_longest_word(words, expected):
    assert_that(simple_functions.the_longest_word(words)).is_equal_to(expected)


def test_the_longest_word_is_in_original_list():
    words = ["hi", "hello", "hey"]
    result = simple_functions.the_longest_word(words)
    assert_that(words).contains(result)


def test_the_longest_word_not_empty():
    words = ["a", "bb", "ccc"]
    result = simple_functions.the_longest_word(words)
    assert_that(result).is_not_empty()


@pytest.mark.parametrize("str1, str2, expected", [
    ("Hello, world!", "world", 7),
    ("banana", "cat", -1),
    ("Python", "", 0),
])
def test_find_substring(str1, str2, expected):
    assert_that(simple_functions.find_substring(str1, str2)).is_equal_to(expected)


def test_find_substring_not_found_returns_negative():
    result = simple_functions.find_substring("apple", "qwe")
    assert_that(result).is_equal_to(-1)


def test_find_substring_result_is_not_greater_than_string_length():
    str1 = "Hello, world!"
    result = simple_functions.find_substring(str1, "world")
    assert_that(result).is_less_than(len(str1))