# src/loader.py
# File and data loading utilities

import json
import csv
# IMPORT ERROR: 'yaml' module is not installed (not in requirements.txt)
import yaml


def load_json(filepath: str) -> dict:
    """Load and return data from a JSON file."""
    with open(filepath, 'r') as f:
        return json.load(f)


def save_json(data: dict, filepath: str) -> None:
    """Save a dictionary to a JSON file."""
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=2)


def load_csv(filepath: str) -> list:
    """Load and return rows from a CSV file as list of dicts."""
    rows = []
    with open(filepath, 'r', newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append(dict(row))
    return rows


def load_yaml(filepath: str) -> dict:
    """Load and return data from a YAML file."""
    with open(filepath, 'r') as f:
        return yaml.safe_load(f)


def load_text(filepath: str) -> str:
    """Load and return contents of a text file."""
    with open(filepath, 'r') as f:
        return f.read()


def save_text(content: str, filepath: str) -> None:
    """Save a string to a text file."""
    with open(filepath, 'w') as f:
        f.write(content)


def file_exists(filepath: str) -> bool:
    """Check if a file exists at the given path."""
    import os
    return os.path.isfile(filepath)
