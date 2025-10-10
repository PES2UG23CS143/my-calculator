#!/usr/bin/env python3
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

    # Binary operations that require two operands
    binary_ops = {"add", "subtract", "multiply", "divide", "power"}

    # Check for missing second operand
    if operation in binary_ops and num2 is None:
        click.echo(f"Error: operation '{operation}' requires two operands.", err=True)
        sys.exit(2)

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
            result = square_root(num1)
        else:
            click.echo(f"Unknown operation: {operation}", err=True)
            sys.exit(2)

        # --- Output formatting ---
        if float(result).is_integer():
            click.echo(int(result))
        else:
            click.echo(f"{result:.2f}")

    except ValueError as e:
        click.echo(f"Error: {e}", err=True)
        sys.exit(1)
    except Exception as e:
        click.echo(f"Unexpected error: {e}", err=True)
        sys.exit(1)


if __name__ == "__main__":
    calculate()
