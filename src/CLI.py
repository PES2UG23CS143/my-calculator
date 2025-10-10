"""
Command Line Interface for Calculator
Example usage:
    python src/cli.py add 5 3
    python src/cli.py subtract 10 4
"""

import sys
import click
from calculator import add, subtract, multiply, divide, power, square_root


@click.command()
@click.argument("operation")
@click.argument("num1", type=float)
@click.argument("num2", type=float, required=False)
def calculate(operation, num1, num2=None):
    """
    Simple calculator CLI using Click.

    OPERATION: one of add, subtract, multiply, divide, power, square_root
    NUM1: first number (always required)
    NUM2: second number (required for all except square_root)
    """

    try:
        # --- Match operation name to function ---
        if operation == "add":
            result = add(num1, num2)
        elif operation == "subtract":
            result = subtract(num1, num2)
        elif operation == "multiply":
            result = multiply(num1, num2)
        elif operation == "divide":
            result = divide(num1, num2)
        elif operation == "power":
            result = power(num1, num2)
        elif operation == "square_root":
            # For square_root, only num1 is needed
            result = square_root(num1)
        else:
            click.echo(f"Unknown operation: {operation}")
            sys.exit(1)

        # --- Output formatting ---
        # If result is an integer (e.g., 8.0 → 8), print as int
        if result == int(result):
            click.echo(int(result))
        else:
            click.echo(f"{result:.2f}")

    except ValueError as e:
        click.echo(f"Error: {e}")
        sys.exit(1)
    except Exception as e:
        click.echo(f"Unexpected error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    calculate()
