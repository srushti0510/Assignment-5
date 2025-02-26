# app/command.py

class Command:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def execute(self):
        raise NotImplementedError("Each command must implement the execute method.")
