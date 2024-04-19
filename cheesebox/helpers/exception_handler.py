def exception_handler(func):
    """
    A decorator that wraps the passed in function and handles exceptions.

    Parameters:
    func (function): The function to wrap.

    Returns:
    function: The function wrapped in a try/except

    Raises:
    SyntaxError: If the wrapped function raises a SyntaxError, returns "✖ Invalid syntax".
    Exception: If the wrapped function raises a general Exception, returns "Error: {str(e)}".
    """
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        
        except SyntaxError:
            return "✖ Invalid syntax"
        except Exception as e:
            return f"Error: {str(e)}"
    return wrapper