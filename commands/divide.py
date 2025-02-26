# commands/divide.py

from commands.command import Command
from calculator.calculator import BaseCalculator

class DivideCommand(Command):
    """Command to divide two numbers."""
    def execute(self):
        return BaseCalculator.divide(self.a, self.b)
