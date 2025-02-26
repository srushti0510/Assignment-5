# app/repl.py

from app.command_handler import handle_command

def repl():
    print("Running REPL mode...")
    print("Available Commands:")
    print(" - add: Adds two numbers.")
    print(" - subtract: Subtracts the second number from the first.")
    print(" - multiply: Multiplies two numbers.")
    print(" - divide: Divides the first number by the second.")
    print(" - exit: Exits the program.")

    while True:
        command_input = input("Enter your command (num1 num2 operation): ")
        
        if command_input.lower() == 'exit':
            print("Exiting REPL mode.")
            break
            
        command_parts = command_input.split()

        if len(command_parts) == 3:
            a_string, b_string, operation = command_parts
            
            try:
                a = float(a_string)
                b = float(b_string)
                
                # Convert to integers if they're whole numbers for display
                a_display = int(a) if a.is_integer() else a
                b_display = int(b) if b.is_integer() else b
                
                result = handle_command(operation, a, b)
                print(result)
            except ValueError:
                print(f"Invalid number input: {a_string} or {b_string} is not a valid number.")
        else:
            print("Invalid command. Format should be: num1 num2 operation")