import json
from pathlib import Path

DATA_FILE = Path(__file__).parent.parent.parent / "data" / "todos.json"

def load_todos():
    """Load to-dos from JSON file."""
    if DATA_FILE.exists():
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return []

def save_todos(todos):
    """Save to-dos to JSON file."""
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(DATA_FILE, 'w') as f:
        json.dump(todos, f, indent=2)