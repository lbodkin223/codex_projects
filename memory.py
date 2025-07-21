"""Memory system for tracking character relationships."""
import json
from typing import Dict

MEMORY_FILE = 'memory.json'


def load_memory() -> Dict:
    """Load memory from the JSON file."""
    try:
        with open(MEMORY_FILE, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {"relationships": {}}


def save_memory(memory: Dict) -> None:
    """Persist memory to disk."""
    with open(MEMORY_FILE, 'w') as f:
        json.dump(memory, f, indent=2)


def update_relationship(memory: Dict, character: str, delta: int) -> None:
    """Update relationship value with a delta."""
    relationships = memory.setdefault("relationships", {})
    relationships[character] = relationships.get(character, 0) + delta
