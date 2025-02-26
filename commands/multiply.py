# commands/multiply.py

from commands.command import Command
from calculator.calculator import BaseCalculator

class MultiplyCommand(Command):
    """Command to multiply two numbers."""
    def execute(self):
        return BaseCalculator.multiply(self.a, self.b)
