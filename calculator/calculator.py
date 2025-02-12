from calculator.calculation import Calculation



class Calculator:
    """Calculator using Calculation class"""

    @staticmethod
    def add(a: float, b: float) -> float:
        return Calculation(a, b, lambda x, y: x + y).perform_calculation()

    @staticmethod
    def subtract(a: float, b: float) -> float:
        return Calculation(a, b, lambda x, y: x - y).perform_calculation()

    @staticmethod
    def multiply(a: float, b: float) -> float:
        return Calculation(a, b, lambda x, y: x * y).perform_calculation()

    @staticmethod
    def divide(a: float, b: float) -> float:
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return Calculation(a, b, lambda x, y: x / y).perform_calculation()
