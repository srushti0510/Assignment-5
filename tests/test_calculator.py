import pytest
from calculator import Calculator

def test_add():
    """Test addition of two numbers."""
    assert Calculator.add(2, 3) == 5

def test_subtract():
    """Test subtraction of two numbers."""
    assert Calculator.subtract(5, 2) == 3

def test_multiply():
    """Test multiplication of two numbers."""
    assert Calculator.multiply(2, 3) == 6

def test_divide():
    """Test division of two numbers."""
    assert Calculator.divide(6, 3) == 2

def test_divide_by_zero():
    """Test division by zero."""
    with pytest.raises(ZeroDivisionError):
        Calculator.divide(5, 0)
