class BaseCalculator:
    """Base class for basic calculator operations."""
    
    @staticmethod
    def add(a: float, b: float) -> float:
        """Add two numbers."""
        return a + b

    @staticmethod
    def subtract(a: float, b: float) -> float:
        """Subtract second number from the first."""
        return a - b

    @staticmethod
    def multiply(a: float, b: float) -> float:
        """Multiply two numbers."""
        return a * b

    @staticmethod
    def divide(a: float, b: float) -> float:
        """Divide the first number by the second, raises ZeroDivisionError if b is 0."""
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return a / b


class Calculator(BaseCalculator):
    """Simple Calculator with basic operations using BaseCalculator."""
    pass
