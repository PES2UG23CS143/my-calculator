def add(a, b):
    """Add two numbers"""
    return a + b


def subtract(a, b):
    """Subtract b from a"""
    return a - b


def multiply(a, b):
    """Multiply two numbers with input validation."""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be numbers")
    return a * b


def divide(a, b):
    """Divide a by b with input validation."""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Division requires numeric inputs")
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b

def power(a, b):
    """Return a raised to the power of b with validation."""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Power requires numeric inputs")
    return a ** b


def square_root(a):
    """Return the square root of a with validation."""
    if not isinstance(a, (int, float)):
        raise TypeError("Square root requires a numeric input")
    if a < 0:
        raise ValueError("Cannot calculate square root of negative number")
    return a ** 0.5
