"""Command-line interface tying together the parser, responder and memory."""
import json
from pathlib import Path

import parser as nlp_parser
import responder
import memory

PROFILE_FILE = 'character.json'


def ensure_sample_profile() -> None:
    """Create a simple sample profile if none exists."""
    if not Path(PROFILE_FILE).exists():
        sample = {
            "name": "Alex",
            "traits": ["friendly", "curious"],
        }
        with open(PROFILE_FILE, 'w') as f:
            json.dump(sample, f, indent=2)


def main() -> None:
    ensure_sample_profile()
    profile = responder.load_profile(PROFILE_FILE)
    mem = memory.load_memory()

    print("Enter text (type 'quit' to exit):")
    while True:
        try:
            line = input('> ').strip()
        except EOFError:
            break
        if line.lower() in {'quit', 'exit'}:
            break
        parsed = nlp_parser.parse_input(line)
        print('Parsed:', parsed)
        response = responder.respond(profile, parsed)
        print('Response:', response)

        # Update memory as simple example
        if parsed['intent'] == 'greet':
            memory.update_relationship(mem, profile['name'], 1)
        elif parsed['intent'] == 'attack':
            memory.update_relationship(mem, profile['name'], -1)

        memory.save_memory(mem)
        print('Memory:', json.dumps(mem, indent=2))

    print('Goodbye!')


if __name__ == '__main__':
    main()
