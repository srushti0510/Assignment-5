import pytest
from calculator.calculations import Calculations  
from calculator.calculation import Calculation   


def test_add_calculation():
    calc = Calculation(2, 3, lambda x, y: x + y)
    Calculations.add_calculation(calc)
    assert Calculations.get_last_calculation() == calc

def test_clear_history():
    Calculations.clear_history()
    assert len(Calculations.history) == 0
