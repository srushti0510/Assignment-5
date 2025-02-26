# app/multiprocessing_calculator.py
import multiprocessing
from app.plugin_loader import PluginLoader

class MultiprocessingCalculator:
    """Calculator that processes commands using multiple CPU cores."""
    
    def __init__(self):
        """Initialize the multiprocessing calculator."""
        self.plugin_loader = PluginLoader()
    
    def _calculate(self, operation, a, b, result_queue):
        """Execute a calculation in a separate process and put the result in the queue."""
        try:
            command = self.plugin_loader.get_command(operation, a, b)
            if command:
                try:
                    result = command.execute()
                    result_queue.put(("success", result))
                except ZeroDivisionError:
                    result_queue.put(("error", "Cannot divide by zero."))
            else:
                result_queue.put(("error", f"Unknown operation: {operation}"))
        except Exception as e:
            result_queue.put(("error", f"Unexpected error: {str(e)}"))

    def calculate(self, operation, a, b):
        """Calculate the result of an operation using a separate process."""
        # Create a queue for the result
        result_queue = multiprocessing.Queue()
        
        # Create and start a new process
        process = multiprocessing.Process(
            target=self._calculate,
            args=(operation, a, b, result_queue)
        )
        process.start()
        
        # Wait for the process to complete (with timeout)
        process.join(timeout=5)
        
        # Check if the process is still alive (timed out)
        if process.is_alive():
            process.terminate()
            process.join()
            return "Calculation timed out."
        
        # Get the result from the queue
        if not result_queue.empty():
            status, result = result_queue.get()
            if status == "success":
                # Format the result
                if isinstance(result, float) and result.is_integer():
                    result = int(result)
                return result
            else:
                return f"An error occurred: {result}"
        else:
            return "Calculation failed with no result."