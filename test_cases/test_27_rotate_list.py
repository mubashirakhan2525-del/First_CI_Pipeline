
import importlib

module = importlib.import_module("27_rotate_list")
rotate_list = module.rotate_list


def test_rotate_right():
    assert rotate_list([1, 2, 3, 4, 5], 2) == [4, 5, 1, 2, 3]


def test_rotate_left():
    assert rotate_list([1, 2, 3, 4, 5], -2) == [3, 4, 5, 1, 2]


def test_k_larger_than_length():
    assert rotate_list([1, 2, 3], 5) == [2, 3, 1]


def test_empty_list():
    assert rotate_list([], 3) == []


def test_zero_rotation():
    assert rotate_list([1, 2, 3], 0) == [1, 2, 3]


def test_original_list_unchanged():
    items = [1, 2, 3, 4]
    result = rotate_list(items, 1)

    assert result == [4, 1, 2, 3]
    assert items == [1, 2, 3, 4]


def test_rotation_equal_to_length():
    assert rotate_list([1, 2, 3], 3) == [1, 2, 3]


def test_single_item():
    assert rotate_list([7], 4) == [7]
