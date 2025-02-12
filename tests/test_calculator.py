import pytest
from calculator import Calculator
from calculator.calculation import Calculation

# Test Calculation class
def test_calculation_add():
    """Test Calculation class with addition"""
    calc = Calculation(5, 3, lambda x, y: x + y)
    assert calc.perform_calculation() == 8

def test_calculation_subtract():
    """Test Calculation class with subtraction"""
    calc = Calculation(10, 4, lambda x, y: x - y)
    assert calc.perform_calculation() == 6

def test_calculation_multiply():
    """Test Calculation class with multiplication"""
    calc = Calculation(6, 7, lambda x, y: x * y)
    assert calc.perform_calculation() == 42

def test_calculation_divide():
    """Test Calculation class with division"""
    calc = Calculation(20, 4, lambda x, y: x / y)
    assert calc.perform_calculation() == 5

# Test Calculator class
def test_calculator_add():
    """Test Calculator add method"""
    assert Calculator.add(2, 3) == 5

def test_calculator_subtract():
    """Test Calculator subtract method"""
    assert Calculator.subtract(10, 5) == 5

def test_calculator_multiply():
    """Test Calculator multiply method"""
    assert Calculator.multiply(4, 3) == 12

def test_calculator_divide():
    """Test Calculator divide method"""
    assert Calculator.divide(20, 5) == 4

def test_calculator_divide_by_zero():
    """Test Calculator division by zero raises ZeroDivisionError"""
    with pytest.raises(ZeroDivisionError):
        Calculator.divide(10, 0)

# Edge case tests
def test_calculator_divide_small():
    """Test Calculator divide method with small decimal numbers"""
    result = Calculator.divide(0.1, 0.2)
    assert result == 0.5

def test_calculator_add_large_numbers():
    """Test Calculator add method with large numbers"""
    result = Calculator.add(1e10, 1e10)
    assert result == 2e10
