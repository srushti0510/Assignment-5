from .calculation import Calculation

class Calculator:
    """Calculator using Calculation class"""

    @staticmethod
    def add(a: float, b: float) -> float:
        """Add two numbers"""
        return Calculation(a, b, lambda x, y: x + y).perform_calculation()

    @staticmethod
    def subtract(a: float, b: float) -> float:
        """Subtract two numbers"""
        return Calculation(a, b, lambda x, y: x - y).perform_calculation()

    @staticmethod
    def multiply(a: float, b: float) -> float:
        """Multiply two numbers"""
        return Calculation(a, b, lambda x, y: x * y).perform_calculation()

    @staticmethod
    def divide(a: float, b: float) -> float:
        """Divide two numbers"""
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return Calculation(a, b, lambda x, y: x / y).perform_calculation()
