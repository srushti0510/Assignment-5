# tests/test_multiprocessing.py
import pytest
from app.multiprocessing_calculator import MultiprocessingCalculator

def test_multiprocessing_calculator_initialization():
    """Test if the multiprocessing calculator initializes correctly."""
    calculator = MultiprocessingCalculator()
    assert calculator is not None
    assert calculator.plugin_loader is not None
    
def test_multiprocessing_calculator_basic_operations():
    """Test if the multiprocessing calculator can perform basic operations."""
    calculator = MultiprocessingCalculator()
    
    # Test add
    result = calculator.calculate("add", 5, 3)
    assert result == 8
    
    # Test subtract
    result = calculator.calculate("subtract", 5, 3)
    assert result == 2
    
    # Test multiply
    result = calculator.calculate("multiply", 5, 3)
    assert result == 15
    
    # Test divide
    result = calculator.calculate("divide", 6, 3)
    assert result == 2
    
def test_multiprocessing_calculator_division_by_zero():
    """Test if the multiprocessing calculator handles division by zero."""
    calculator = MultiprocessingCalculator()
    
    result = calculator.calculate("divide", 5, 0)
    assert isinstance(result, str)
    assert "Cannot divide by zero" in result
    
def test_multiprocessing_calculator_unknown_operation():
    """Test if the multiprocessing calculator handles unknown operations."""
    calculator = MultiprocessingCalculator()
    
    result = calculator.calculate("unknown", 5, 3)
    assert isinstance(result, str)
    assert "Unknown operation" in result