# src/validator.py
# Validation functions for the application

from typing import Optional
from re import match
from string import ascii_letters


def validate_username(username: str) -> bool
    """Validate that username only contains alphanumeric chars."""
    # SYNTAX ERROR: missing colon at line 8 (def line)
    if not username:
        return False
    return all(c.isalnum() or c == '_' for c in username)


def validate_email(email: str) -> bool:
    """Validate a basic email address format."""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(match(pattern, email))


def validate_phone(phone: str) -> bool:
    """Validate a phone number (10 digits)."""
    digits = ''.join(filter(str.isdigit, phone))
    return len(digits) == 10


def validate_password(password: str) -> bool:
    """Validate password is at least 8 chars with a digit."""
    if len(password) < 8:
        return False
    return any(c.isdigit() for c in password)


def validate_age(age: int) -> bool:
    """Validate age is between 0 and 120."""
    return 0 <= age <= 120


def validate_url(url: str) -> bool:
    """Validate that a URL starts with http or https."""
    return url.startswith('http://') or url.startswith('https://')


def sanitize_string(s: str) -> str:
    """Remove non-ASCII letters from string."""
    return ''.join(c for c in s if c in ascii_letters + ' ')
