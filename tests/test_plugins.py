# tests/test_plugins.py
import pytest
from app.plugin_loader import PluginLoader

def test_plugin_loader_initialization():
    """Test if the plugin loader initializes correctly."""
    loader = PluginLoader()
    assert loader is not None
    assert loader.command_plugins is not None
    
def test_plugin_loader_loads_commands():
    """Test if the plugin loader loads all calculator commands."""
    loader = PluginLoader()
    commands = loader.get_available_commands()
    
    # Check that all basic operations are loaded
    assert "add" in commands
    assert "subtract" in commands
    assert "multiply" in commands
    assert "divide" in commands
    
def test_plugin_loader_get_command():
    """Test if the plugin loader can retrieve command instances."""
    loader = PluginLoader()
    
    # Test valid commands
    add_command = loader.get_command("add", 5, 3)
    assert add_command is not None
    assert add_command.execute() == 8.0
    
    subtract_command = loader.get_command("subtract", 5, 3)
    assert subtract_command is not None
    assert subtract_command.execute() == 2.0
    
    # Test invalid command
    invalid_command = loader.get_command("invalid", 5, 3)
    assert invalid_command is None

def test_menu_command(capsys):
    """Test if the menu command displays all available commands."""
    from app.command_handler import handle_command
    
    # Test menu command
    menu = handle_command("menu", 0, 0)
    
    # Check if menu contains all basic operations
    assert "add: Adds two numbers" in menu
    assert "subtract: Subtracts" in menu
    assert "multiply: Multiplies" in menu
    assert "divide: Divides" in menu
    assert "menu: Shows this menu" in menu
    