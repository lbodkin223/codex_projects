"""Generate character responses based on parsed input and character profile."""
import json
from typing import Dict


def load_profile(path: str) -> Dict:
    """Load a character profile from a JSON file."""
    with open(path, 'r') as f:
        return json.load(f)


def respond(profile: Dict, parsed: Dict[str, str]) -> str:
    """Return a textual response based on the profile and parsed input."""
    name = profile.get('name', 'Someone')
    intent = parsed.get('intent')
    tone = parsed.get('tone')

    if intent == 'greet':
        response = f"{name} smiles and greets you back."
    elif intent == 'attack':
        response = f"{name} dodges defensively, looking startled."
    elif intent == 'help':
        response = f"{name} nods and offers assistance."
    else:
        response = f"{name} listens." 

    if tone == 'question':
        response += " They seem thoughtful about your question."
    elif tone == 'polite':
        response += " They appreciate your manners."

    return response
