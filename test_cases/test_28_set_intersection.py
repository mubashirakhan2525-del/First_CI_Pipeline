
import importlib

module = importlib.import_module("28_set_intersection")
set_intersection = module.set_intersection


def test_basic_intersection():
    assert set_intersection({1, 2, 3}, {2, 3, 4}) == {2, 3}


def test_no_common_elements():
    assert set_intersection({1, 2}, {3, 4}) == set()


def test_identical_sets():
    assert set_intersection({1, 2, 3}, {1, 2, 3}) == {1, 2, 3}


def test_empty_first_set():
    assert set_intersection(set(), {1, 2}) == set()


def test_empty_second_set():
    assert set_intersection({1, 2}, set()) == set()


def test_single_common_element():
    assert set_intersection({5, 10, 15}, {10, 20, 30}) == {10}


def test_original_sets_unchanged():
    first = {1, 2, 3}
    second = {2, 3, 4}

    set_intersection(first, second)

    assert first == {1, 2, 3}
    assert second == {2, 3, 4}
