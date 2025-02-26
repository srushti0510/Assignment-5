from commands.add import AddCommand
from commands.subtract import SubtractCommand
from commands.multiply import MultiplyCommand
from commands.divide import DivideCommand

# main.py
from app.command_handler import handle_command, get_menu
from app.plugin_loader import PluginLoader

def calculate_and_print(a_string, b_string, operation_string):
    try:
        a = float(a_string)
        b = float(b_string)
    except ValueError:
        print(f"Invalid number input: {a_string} or {b_string} is not a valid number.")
        return

    # Ensure integers are displayed as integers
    a_display = int(a) if a.is_integer() else a
    b_display = int(b) if b.is_integer() else b

    # Special case for menu command
    if operation_string == "menu":
        print(get_menu())
        return

    # Use the command handler to process the operation
    result = handle_command(operation_string, a, b)
    print(result)


def repl():
    """Read-Eval-Print Loop for calculator."""
    print("Running REPL mode...\n")
    print(get_menu())
    
    while True:
        # Get user input
        user_input = input("\nEnter operation and numbers (e.g., '5 3 add' or 'menu'): ").strip()
        
        # If the user types 'exit', break the loop and exit
        if user_input.lower() == 'exit':
            print("Exiting REPL mode.")
            break

        # Handle menu command
        if user_input.lower() == 'menu':
            print(get_menu())
            continue

        # Split the input into components
        parts = user_input.split()
        if len(parts) != 3:
            print("Invalid input. Please enter in the format: <number> <number> <operation>")
            continue

        # The test expects the format "1 4 add"
        a_string, b_string, operation_string = parts
        
        # Call calculate_and_print to process the input and print the result
        calculate_and_print(a_string, b_string, operation_string)

if __name__ == "__main__":
     print("Select mode:")
     print("1. Regular calculator")
     print("2. Calculator with multiprocessing")
     choice = input("Enter choice (1 or 2): ")
     
     if choice == "2":
         from app.multiprocessing_repl import multiprocessing_repl
         multiprocessing_repl()
     else:
         repl()