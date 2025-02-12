class Calculation:
    """Class to store a single calculation"""

    def __init__(self, a: float, b: float, operation):
        self.a = a
        self.b = b
        self.operation = operation

    def perform_calculation(self) -> float:
        return self.operation(self.a, self.b)
