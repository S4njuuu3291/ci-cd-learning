import pytest

from src.main import add, divide, multiply


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0


def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(0, 100) == 0


def test_divide():
    assert divide(10, 2) == 5
    assert divide(1, 4) == 0.25


def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)
