
import importlib
import pytest

module = importlib.import_module("25_max_min_list")
find_max_min = module.find_max_min


def test_basic_list():
    assert find_max_min([3, 8, 1, 9, 4]) == (9, 1)


def test_negative_numbers():
    assert find_max_min([-5, -2, -10]) == (-2, -10)


def test_all_same_numbers():
    assert find_max_min([4, 4, 4]) == (4, 4)


def test_single_number():
    assert find_max_min([7]) == (7, 7)


def test_mixed_numbers():
    assert find_max_min([-3, 0, 12, -8]) == (12, -8)


def test_empty_list():
    with pytest.raises(ValueError):
        find_max_min([])
