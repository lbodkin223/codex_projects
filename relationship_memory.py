import json
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Dict

@dataclass
class RelationshipStats:
    """In-memory representation of relationship statistics."""
    trust: float = 0.5
    attraction: float = 0.5
    respect: float = 0.5

    def apply_deltas(self, deltas: Dict[str, float]) -> None:
        """Apply delta changes to the stats, clamping values between 0 and 1."""
        for stat, delta in deltas.items():
            if hasattr(self, stat):
                value = getattr(self, stat) + delta
                setattr(self, stat, max(0.0, min(1.0, value)))

class RelationshipMemory:
    """Handles loading, updating, and saving relationship stats."""

    def __init__(self, file_path: str = "relationship_state.json") -> None:
        self.file_path = Path(file_path)
        self.stats = RelationshipStats()
        self.load()

    def load(self) -> None:
        """Load stats from disk if the file exists."""
        if self.file_path.exists():
            with self.file_path.open("r", encoding="utf-8") as fh:
                data = json.load(fh)
            self.stats = RelationshipStats(**data)

    def save(self) -> None:
        """Persist stats to disk."""
        with self.file_path.open("w", encoding="utf-8") as fh:
            json.dump(asdict(self.stats), fh, indent=2)

    ACTION_EFFECTS = {
        "compliment": {"trust": 0.05, "attraction": 0.1, "respect": 0.05},
        "kind_act": {"trust": 0.1, "respect": 0.1},
        "insult": {"trust": -0.1, "attraction": -0.1, "respect": -0.1},
        "betrayal": {"trust": -0.2, "respect": -0.2},
    }

    def update(self, action: str) -> None:
        """Update stats based on a user action and save the result."""
        deltas = self.ACTION_EFFECTS.get(action, {})
        if deltas:
            self.stats.apply_deltas(deltas)
            self.save()

if __name__ == "__main__":
    import sys

    memory = RelationshipMemory()
    for action in sys.argv[1:]:
        memory.update(action)
    print(asdict(memory.stats))
