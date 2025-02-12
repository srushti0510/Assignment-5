from .calculation import Calculation

class Calculations:
    """Class to store and manage calculation history"""
    
    history = []

    @classmethod
    def add_calculation(cls, calculation: Calculation):
        """Adds a calculation to history"""
        cls.history.append(calculation)

    @classmethod
    def get_last_calculation(cls):
        """Returns the last calculation from history"""
        return cls.history[-1] if cls.history else None

    @classmethod
    def clear_history(cls):
        """Clears all history of calculations"""
        cls.history.clear()

    @classmethod
    def get_history(cls):
        """Returns all the history of calculations"""
        return cls.history
