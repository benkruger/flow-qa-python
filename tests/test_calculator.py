from src.calculator import Calculator


def test_add():
    calc = Calculator()
    assert calc.add(2, 3) == 5


def test_add_negative():
    calc = Calculator()
    assert calc.add(2, -3) == -1


def test_multiply():
    calc = Calculator()
    assert calc.multiply(3, 4) == 12


def test_multiply_negative():
    calc = Calculator()
    assert calc.multiply(3, -4) == -12


def test_multiply_both_negative():
    calc = Calculator()
    assert calc.multiply(-3, -4) == 12


def test_multiply_by_zero():
    calc = Calculator()
    assert calc.multiply(5, 0) == 0
