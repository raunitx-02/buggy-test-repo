# tests/test_calculator.py
import pytest
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from calculator import add, subtract, multiply, divide, power, modulo, average, factorial, is_prime


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0


def test_subtract():
    assert subtract(10, 4) == 6
    assert subtract(0, 5) == -5


def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(0, 100) == 0


def test_divide():
    assert divide(10, 2) == 5.0
    assert divide(7, 2) == pytest.approx(3.5)


def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(5, 0)


def test_power():
    # This test FAILS because power() has a LOGIC BUG (uses exp+1)
    assert power(2, 3) == 8   # actual returns 16 due to the bug
    assert power(5, 2) == 25  # actual returns 125 due to the bug


def test_modulo():
    assert modulo(10, 3) == 1
    assert modulo(9, 3) == 0


def test_modulo_by_zero():
    with pytest.raises(ValueError):
        modulo(5, 0)


def test_average():
    assert average([1, 2, 3, 4, 5]) == 3.0
    assert average([10]) == 10.0


def test_average_empty():
    with pytest.raises(ValueError):
        average([])


def test_factorial():
    assert factorial(0) == 1
    assert factorial(5) == 120
    assert factorial(10) == 3628800


def test_factorial_negative():
    with pytest.raises(ValueError):
        factorial(-1)


def test_is_prime():
    assert is_prime(2) is True
    assert is_prime(7) is True
    assert is_prime(11) is True
    assert is_prime(1) is False
    assert is_prime(4) is False
    assert is_prime(9) is False
