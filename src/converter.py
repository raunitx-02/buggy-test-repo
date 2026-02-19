# src/converter.py
# Unit conversion functions


def celsius_to_fahrenheit(celsius: float) -> float:
    """Convert Celsius to Fahrenheit."""
    return (celsius * 9 / 5) + 32


def fahrenheit_to_celsius(fahrenheit: float) -> float:
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5 / 9


def km_to_miles(km: float) -> float:
    """Convert kilometers to miles."""
    return km * 0.621371


def miles_to_km(miles: float) -> float:
    """Convert miles to kilometers."""
    return miles / 0.621371


def kg_to_pounds(kg: float) -> float:
    """Convert kilograms to pounds."""
    return kg * 2.20462


def seconds_to_hms(seconds: int) -> str:
    """Convert seconds to HH:MM:SS string."""
    # TYPE_ERROR: returns a list instead of a string
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    secs = seconds % 60
    return [hours, minutes, secs]  # Should be f"{hours:02}:{minutes:02}:{secs:02}"


def liters_to_gallons(liters: float) -> float:
    """Convert liters to US gallons."""
    return liters * 0.264172


def gallons_to_liters(gallons: float) -> float:
    """Convert US gallons to liters."""
    return gallons / 0.264172


def bytes_to_mb(byte_count: int) -> float:
    """Convert bytes to megabytes."""
    return byte_count / (1024 * 1024)
