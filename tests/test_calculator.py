import pytest

from src.calculator import Calculator


def test_add():
    calc = Calculator()
    assert calc.add(2, 3) == 5


def test_add_negative():
    calc = Calculator()
    assert calc.add(2, -3) == -1


def test_subtract():
    calc = Calculator()
    assert calc.subtract(5, 3) == 2


def test_subtract_negative():
    calc = Calculator()
    assert calc.subtract(2, -3) == 5


def test_add_type_error():
    calc = Calculator()
    with pytest.raises(TypeError, match="must be numeric"):
        calc.add("a", 1)


def test_subtract_type_error():
    calc = Calculator()
    with pytest.raises(TypeError, match="must be numeric"):
        calc.subtract(1, "b")
