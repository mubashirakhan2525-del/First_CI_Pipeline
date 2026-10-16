
import importlib
import pytest

module = importlib.import_module("30_decimal_to_binary")
decimal_to_binary = module.decimal_to_binary


def test_convert_10():
    assert decimal_to_binary(10) == "1010"


def test_convert_0():
    assert decimal_to_binary(0) == "0"


def test_convert_1():
    assert decimal_to_binary(1) == "1"


def test_convert_2():
    assert decimal_to_binary(2) == "10"


def test_convert_15():
    assert decimal_to_binary(15) == "1111"


def test_convert_100():
    assert decimal_to_binary(100) == "1100100"


def test_negative_number():
    with pytest.raises(ValueError):
        decimal_to_binary(-5)


def test_large_number():
    assert decimal_to_binary(255) == "11111111"
