import re

def extended_eval(expression):
    """
    Evaluates a mathematical expression, extending the built-in eval function to interpret '2(3)' as '2 * (3)'.

    Args:
        expression (str): The mathematical expression to evaluate.

    Returns:
        The result of the evaluated expression.
    """
    expression = re.sub(r'(\d)\s*\(', r'\1 * (', expression)
    return eval(expression)