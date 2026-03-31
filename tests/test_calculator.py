import pytest

from src.calculator import Calculator


def test_add():
    calc = Calculator()
    assert calc.add(2, 3) == 5


def test_add_negative():
    calc = Calculator()
    assert calc.add(2, -3) == -1


def test_divide():
    calc = Calculator()
    assert calc.divide(10, 2) == 5.0


def test_divide_float_result():
    calc = Calculator()
    assert calc.divide(7, 2) == 3.5


def test_divide_by_zero():
    calc = Calculator()
    with pytest.raises(ZeroDivisionError):
        calc.divide(10, 0)


def test_divide_negative():
    calc = Calculator()
    assert calc.divide(-6, 3) == -2.0
