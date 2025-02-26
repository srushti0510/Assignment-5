# app/multiprocessing_repl.py
from app.command_handler import get_menu
from app.multiprocessing_calculator import MultiprocessingCalculator

def multiprocessing_repl():
    """Read-Eval-Print Loop for calculator with multiprocessing support."""
    calculator = MultiprocessingCalculator()
    
    print("Running REPL mode with multiprocessing...\n")
    print(get_menu())
    print(" - mp: Toggle multiprocessing mode (currently ON)")
    
    multiprocessing_enabled = True
    
    while True:
        # Get user input
        user_input = input("\nEnter operation and numbers (e.g., '5 3 add' or 'menu'): ").strip()
        
        # Handle exit command
        if user_input.lower() == 'exit':
            print("Exiting REPL mode.")
            break

        # Handle menu command
        if user_input.lower() == 'menu':
            print(get_menu())
            print(f" - mp: Toggle multiprocessing mode (currently {'ON' if multiprocessing_enabled else 'OFF'})")
            continue
            
        # Handle multiprocessing toggle
        if user_input.lower() == 'mp':
            multiprocessing_enabled = not multiprocessing_enabled
            print(f"Multiprocessing mode {'enabled' if multiprocessing_enabled else 'disabled'}.")
            continue

        # Parse input
        parts = user_input.split()
        if len(parts) != 3:
            print("Invalid input. Please enter in the format: <number> <number> <operation>")
            continue

        # The expected format is "1 4 add"
        try:
            a_string, b_string, operation_string = parts
            a = float(a_string)
            b = float(b_string)
            
            # Ensure integers are displayed as integers
            a_display = int(a) if a.is_integer() else a
            b_display = int(b) if b.is_integer() else b
            
            if multiprocessing_enabled:
                # Use multiprocessing calculator
                result = calculator.calculate(operation_string, a, b)
                if isinstance(result, str) and result.startswith("An error"):
                    print(result)
                else:
                    print(f"The result of {a_display} {operation_string} {b_display} is equal to {result}")
            else:
                # Use regular calculator
                from app.command_handler import handle_command
                result = handle_command(operation_string, a, b)
                print(result)
                
        except ValueError:
            print(f"Invalid number input: {a_string} or {b_string} is not a valid number.")

