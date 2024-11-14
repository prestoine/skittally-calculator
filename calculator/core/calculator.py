# calculator/core/calculator.py
class Calculator:
    """Core calculator logic handling mathematical operations."""
    
    @staticmethod
    def evaluate(expression: str) -> str:
        """Evaluates a mathematical expression and returns the result."""
        try:
            # In a production environment, you'd want to use a safer evaluation method
            # than eval(), like the `ast.literal_eval()` or a proper parser
            result = str(eval(expression))
            return result
        except Exception as e:
            return "Error"
