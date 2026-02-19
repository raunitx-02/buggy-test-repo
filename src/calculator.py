# src/calculator.py
# Calculator functions for the application


def add(a: float, b: float) -> float:
    """Return the sum of a and b."""
    return a + b


def subtract(a: float, b: float) -> float:
    """Return the difference of a and b."""
    return a - b


def multiply(a: float, b: float) -> float:
    """Return the product of a and b."""
    return a * b


def divide(a: float, b: float) -> float:
    """Return the quotient of a divided by b."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def power(base: float, exp: int) -> float:
    """Return base raised to the power of exp."""
    # LOGIC ERROR: should be base ** exp, not base ** (exp + 1)
    return base ** (exp + 1)


def modulo(a: int, b: int) -> int:
    """Return a modulo b."""
    if b == 0:
        raise ValueError("Cannot modulo by zero")
    return a % b


def average(numbers: list) -> float:
    """Return the average of a list of numbers."""
    if not numbers:
        raise ValueError("Cannot compute average of empty list")
    return sum(numbers) / len(numbers)


def factorial(n: int) -> int:
    """Return the factorial of n."""
    if n < 0:
        raise ValueError("Factorial undefined for negative numbers")
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def is_prime(n: int) -> bool:
    """Return True if n is a prime number."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
