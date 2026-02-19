# tests/test_validator.py
import pytest
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

# NOTE: validator.py has a SYNTAX error so these tests will FAIL until it is fixed
try:
    from validator import validate_email, validate_phone, validate_password, validate_age, validate_url, sanitize_string
    IMPORT_OK = True
except SyntaxError:
    IMPORT_OK = False


def test_validate_email_valid():
    assert IMPORT_OK, "validator.py has syntax error - fix it first"
    assert validate_email("test@example.com") is True


def test_validate_email_invalid():
    assert IMPORT_OK, "validator.py has syntax error - fix it first"
    assert validate_email("not-an-email") is False


def test_validate_phone_valid():
    assert IMPORT_OK, "validator.py has syntax error - fix it first"
    assert validate_phone("9876543210") is True


def test_validate_phone_invalid():
    assert IMPORT_OK, "validator.py has syntax error - fix it first"
    assert validate_phone("123") is False


def test_validate_password_valid():
    assert IMPORT_OK, "validator.py has syntax error - fix it first"
    assert validate_password("secureP4ss") is True


def test_validate_password_too_short():
    assert IMPORT_OK, "validator.py has syntax error - fix it first"
    assert validate_password("short") is False


def test_validate_age_valid():
    assert IMPORT_OK, "validator.py has syntax error - fix it first"
    assert validate_age(25) is True


def test_validate_age_invalid():
    assert IMPORT_OK, "validator.py has syntax error - fix it first"
    assert validate_age(-1) is False
    assert validate_age(200) is False


def test_validate_url_valid():
    assert IMPORT_OK, "validator.py has syntax error - fix it first"
    assert validate_url("https://example.com") is True


def test_validate_url_invalid():
    assert IMPORT_OK, "validator.py has syntax error - fix it first"
    assert validate_url("ftp://bad.com") is False


def test_sanitize_string():
    assert IMPORT_OK, "validator.py has syntax error - fix it first"
    result = sanitize_string("hello 123!")
    assert result == "hello "
