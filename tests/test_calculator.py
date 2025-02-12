import pytest
from calculator.calculations import Calculations
from calculator.calculation import Calculation
from calculator.calculator import Calculator


def test_add_calculation():
    """Test the add_calculation method"""
    calc = Calculation(2, 3, lambda x, y: x + y)
    Calculations.add_calculation(calc)
    assert Calculations.get_last_calculation() == calc


def test_clear_history():
    """Test the clear_history method"""
    calc1 = Calculation(2, 3, lambda x, y: x + y)
    calc2 = Calculation(10, 4, lambda x, y: x - y)
    
    # Add calculations to history
    Calculations.add_calculation(calc1)
    Calculations.add_calculation(calc2)
    
    # Clear history
    Calculations.clear_history()
    
    # Assert that history is now empty
    assert len(Calculations.history) == 0


def test_get_last_calculation():
    """Test the get_last_calculation method"""
    calc1 = Calculation(2, 3, lambda x, y: x + y)
    calc2 = Calculation(10, 4, lambda x, y: x - y)
    
    # Add calculations to history
    Calculations.add_calculation(calc1)
    Calculations.add_calculation(calc2)
    
    # Check that the last calculation is calc2
    assert Calculations.get_last_calculation() == calc2
    
    # Clear the history and check the result
    Calculations.clear_history()
    assert Calculations.get_last_calculation() is None  # Should return None when no calculations are available


def test_add_method():
    """Test Calculator add method"""
    assert Calculator.add(2, 3) == 5


def test_subtract_method():
    """Test Calculator subtract method"""
    assert Calculator.subtract(5, 3) == 2


def test_multiply_method():
    """Test Calculator multiply method"""
    assert Calculator.multiply(2, 3) == 6


def test_divide_method():
    """Test Calculator divide method"""
    assert Calculator.divide(6, 3) == 2


def test_divide_by_zero_method():
    """Test Calculator divide method raises ZeroDivisionError"""
    with pytest.raises(ZeroDivisionError):
        Calculator.divide(5, 0)


def test_calculation_add_method():
    """Test Calculation class with addition"""
    calc = Calculation(5, 3, lambda x, y: x + y)
    assert calc.perform_calculation() == 8


def test_calculation_subtract_method():
    """Test Calculation class with subtraction"""
    calc = Calculation(10, 4, lambda x, y: x - y)
    assert calc.perform_calculation() == 6


def test_calculation_multiply_method():
    """Test Calculation class with multiplication"""
    calc = Calculation(6, 7, lambda x, y: x * y)
    assert calc.perform_calculation() == 42


def test_calculation_divide_method():
    """Test Calculation class with division"""
    calc = Calculation(20, 4, lambda x, y: x / y)
    assert calc.perform_calculation() == 5


def test_history_attribute():
    """Test if history attribute stores calculations correctly"""
    # Create some Calculation instances
    calc1 = Calculation(5, 3, lambda x, y: x + y)
    calc2 = Calculation(8, 2, lambda x, y: x - y)
    
    # Add them to history
    Calculations.add_calculation(calc1)
    Calculations.add_calculation(calc2)
    
    # Check if the history contains the calculations
    assert Calculations.history == [calc1, calc2]
