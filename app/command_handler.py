from commands.add import AddCommand
from commands.subtract import SubtractCommand
from commands.multiply import MultiplyCommand
from commands.divide import DivideCommand
from app.plugin_loader import PluginLoader

plugin_loader = PluginLoader()

def handle_command(command, a, b):
    """Handle user commands for calculator operations using the plugin system."""
    
    # Check if the command is "menu"
    if command == "menu":
        return get_menu()
    
    # Get the command instance from the plugin loader
    command_instance = plugin_loader.get_command(command, a, b)
    
    if command_instance:
        try:
            result = command_instance.execute()
            
            # Ensure that we print the result without a decimal point for whole numbers
            if result.is_integer():
                result = int(result)
            
            # Format the display values as integers if they're whole numbers
            a_display = int(a) if a.is_integer() else a
            b_display = int(b) if b.is_integer() else b
            
            return f"The result of {a_display} {command} {b_display} is equal to {result}"
        except ZeroDivisionError:
            return "An error occurred: Cannot divide by zero."
    else:
        return f"Unknown operation: {command}"

def get_menu():
    """Return a formatted menu of available commands."""
    commands = plugin_loader.get_available_commands() + ["menu", "exit"]
    
    menu_text = "Available Commands:\n"
    for cmd in commands:
        if cmd == "add":
            menu_text += " - add: Adds two numbers.\n"
        elif cmd == "subtract":
            menu_text += " - subtract: Subtracts the second number from the first.\n"
        elif cmd == "multiply":
            menu_text += " - multiply: Multiplies two numbers.\n"
        elif cmd == "divide":
            menu_text += " - divide: Divides the first number by the second.\n"
        elif cmd == "menu":
            menu_text += " - menu: Shows this menu.\n"
        elif cmd == "exit":
            menu_text += " - exit: Exits the program.\n"
    
    return menu_text.strip()
