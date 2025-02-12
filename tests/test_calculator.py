import pytest
from calculator import Calculator

def test_add():
    assert Calculator.add(2, 3) == 5

def test_subtract():
    assert Calculator.subtract(5, 2) == 3

def test_multiply():
    assert Calculator.multiply(2, 3) == 6

def test_divide():
    assert Calculator.divide(6, 3) == 2

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        Calculator.divide(5, 0)
