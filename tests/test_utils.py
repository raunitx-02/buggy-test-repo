# tests/test_utils.py
import pytest
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from utils import greet, flatten, deep_copy_dict, to_json, calculate_sqrt, get_random, ordered_keys, reduce_sum, get_file_stem


def test_greet_returns_string():
    result = greet("Raunit")
    assert isinstance(result, str)
    assert "Raunit" in result


def test_greet_format():
    assert greet("Alice") == "Hello, Alice!"


def test_flatten_basic():
    assert flatten([[1, 2], [3, 4]]) == [1, 2, 3, 4]


def test_flatten_empty():
    assert flatten([]) == []


def test_deep_copy_dict():
    original = {"a": [1, 2, 3]}
    copy = deep_copy_dict(original)
    copy["a"].append(4)
    assert len(original["a"]) == 3


def test_to_json():
    data = {"key": "value"}
    result = to_json(data)
    assert isinstance(result, str)
    assert "key" in result


def test_calculate_sqrt():
    assert calculate_sqrt(9.0) == pytest.approx(3.0)


def test_ordered_keys():
    d = {"b": 2, "a": 1, "c": 3}
    result = ordered_keys(d)
    assert list(result.keys()) == ["a", "b", "c"]


def test_reduce_sum():
    assert reduce_sum([1, 2, 3, 4, 5]) == 15


def test_reduce_sum_empty():
    assert reduce_sum([]) == 0


def test_get_file_stem():
    assert get_file_stem("hello.py") == "hello"
    assert get_file_stem("/path/to/file.txt") == "file"
