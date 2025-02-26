# commands/add.py

from commands.command import Command
from calculator.calculator import BaseCalculator

class AddCommand(Command):
    """Command to add two numbers."""
    def execute(self):
        return BaseCalculator.add(self.a, self.b)

