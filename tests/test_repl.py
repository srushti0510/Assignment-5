import pytest
from main import repl  # Import repl function from main.py

def test_add_repl(monkeypatch, capsys):
    # Simulate user input for '1 4 add' and 'exit' for stopping the REPL loop
    inputs = iter(["1 4 add", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    repl()  # Call the REPL function

    # Capture the output
    captured = capsys.readouterr()

    # Check if the expected output is in the captured output
    assert "The result of 1 add 4 is equal to 5" in captured.out

def test_divide_by_zero_repl(monkeypatch, capsys):
    # Simulate user input for '1 0 divide' which should raise a divide by zero error
    inputs = iter(["1 0 divide", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    repl()  # Call the REPL function

    # Capture the output
    captured = capsys.readouterr()

    # Check if the error message for division by zero is in the captured output
    assert "An error occurred: Cannot divide by zero." in captured.out
