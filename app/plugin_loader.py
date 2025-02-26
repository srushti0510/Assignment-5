# app/plugin_loader.py
import os
import importlib
import inspect

class PluginLoader:
    """Dynamically loads command plugins from a directory."""
    
    def __init__(self, plugin_dir="commands"):
        """Initialize the plugin loader with the directory containing plugins."""
        self.plugin_dir = plugin_dir
        self.command_plugins = {}
        self.load_plugins()
    
    def load_plugins(self):
        """Dynamically load all command plugins from the plugin directory."""
        # Get the absolute path to the plugin directory
        plugin_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), self.plugin_dir)
        
        # Get all Python files in the plugin directory
        plugin_files = [f[:-3] for f in os.listdir(plugin_path) 
                      if f.endswith('.py') and not f.startswith('__')]
        
        for plugin_name in plugin_files:
            # Import the module
            module_path = f"{self.plugin_dir}.{plugin_name}"
            try:
                module = importlib.import_module(module_path)
                
                # Look for command classes in the module
                for name, obj in inspect.getmembers(module):
                    # Check if it's a class and ends with "Command"
                    if inspect.isclass(obj) and name.endswith("Command"):
                        # Extract operation name from class name (e.g., AddCommand -> add)
                        operation = name[:-7].lower()
                        self.command_plugins[operation] = obj
                        print(f"Loaded plugin: {operation}")
            except ImportError as e:
                print(f"Error loading plugin {plugin_name}: {str(e)}")
    
    def get_command(self, operation, a, b):
        """Get a command instance for the specified operation."""
        if operation in self.command_plugins:
            return self.command_plugins[operation](a, b)
        return None
    
    def get_available_commands(self):
        """Return a list of available command operations."""
        return list(self.command_plugins.keys())