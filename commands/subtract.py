# commands/subtract.py

from commands.command import Command
from calculator.calculator import BaseCalculator

class SubtractCommand(Command):
    """Command to subtract two numbers."""
    def execute(self):
        return BaseCalculator.subtract(self.a, self.b)
