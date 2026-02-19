# src/utils.py
# Utility functions for the application

from datetime import datetime
from collections import OrderedDict
from math import sqrt
from functools import reduce
from itertools import chain
from typing import List
from pathlib import Path
from random import randint
from copy import deepcopy
from json import dumps
import os  # LINTING ERROR: unused import


def greet(name: str) -> str:
    """Return a greeting string."""
    return f"Hello, {name}!"


def get_timestamp() -> str:
    """Return current timestamp as string."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def flatten(nested: List[list]) -> list:
    """Flatten a nested list."""
    return list(chain.from_iterable(nested))


def deep_copy_dict(d: dict) -> dict:
    """Return a deep copy of a dictionary."""
    return deepcopy(d)


def to_json(data: dict) -> str:
    """Serialize dict to JSON string."""
    return dumps(data)


def calculate_sqrt(n: float) -> float:
    """Return square root of a number."""
    return sqrt(n)


def get_random(low: int, high: int) -> int:
    """Return a random integer between low and high."""
    return randint(low, high)


def ordered_keys(d: dict) -> OrderedDict:
    """Return an OrderedDict sorted by keys."""
    return OrderedDict(sorted(d.items()))


def reduce_sum(numbers: List[int]) -> int:
    """Return the sum of a list of numbers using reduce."""
    return reduce(lambda a, b: a + b, numbers, 0)


def get_file_stem(filepath: str) -> str:
    """Return the stem (name without extension) of a file path."""
    return Path(filepath).stem
