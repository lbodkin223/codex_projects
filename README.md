# Story Engine

This project is a minimal terminal-based story engine that demonstrates a simple
pipeline of parsing natural language, generating a character response and storing
relationship memory.

## Files

- `parser.py` – converts a line of natural language into a structured dictionary
  containing `intent`, `tone`, `emotion` and `target`.
- `responder.py` – produces a character response based on a JSON profile and the
  parsed input.
- `memory.py` – manages relationship values that persist between interactions.
- `main.py` – command line interface that ties everything together and saves a
  sample character profile if one does not exist.

## Usage

Run the application with:

```bash
python main.py
```

Type text at the prompt and observe the parser output, the generated response
and memory updates saved to `memory.json`.
