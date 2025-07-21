"""Simple natural language parser for the story engine."""
from typing import Dict


def parse_input(text: str) -> Dict[str, str]:
    """Parse raw text and return structured data.

    Args:
        text: Raw user input.

    Returns:
        Dictionary with keys: intent, tone, emotion, target.
    """
    lowered = text.lower()
    data = {
        "intent": "talk",
        "tone": "neutral",
        "emotion": "neutral",
        "target": "none",
    }

    # Determine intent based on simple keywords
    if any(word in lowered for word in ["attack", "hit", "punch"]):
        data["intent"] = "attack"
    elif any(word in lowered for word in ["hello", "hi", "greet"]):
        data["intent"] = "greet"
    elif "help" in lowered:
        data["intent"] = "help"

    # Determine tone
    if lowered.endswith("?"):
        data["tone"] = "question"
    elif any(word in lowered for word in ["please", "kindly"]):
        data["tone"] = "polite"

    # Determine emotion
    if any(word in lowered for word in ["love", "like"]):
        data["emotion"] = "positive"
    elif any(word in lowered for word in ["hate", "anger", "angry"]):
        data["emotion"] = "negative"

    # Target extraction: look for words after '@'
    if "@" in text:
        try:
            at_index = text.index("@")
            target = text[at_index + 1 :].split()[0]
            data["target"] = target
        except Exception:
            pass
    elif "you" in lowered:
        data["target"] = "you"

    return data
