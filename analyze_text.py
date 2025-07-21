"""Basic NLP utilities for extracting intent, tone, and emotion from text."""

import re
from typing import Dict


def extract_intent_tone_emotion(text: str) -> Dict[str, str]:
    """Return simple heuristics for intent, tone, and emotion.

    Parameters
    ----------
    text : str
        Input text from the user.

    Returns
    -------
    Dict[str, str]
        Dictionary containing 'intent', 'tone', and 'emotion'.
    """
    lower_text = text.lower()

    # Intent detection
    if re.search(r"\b(hi|hello|hey|greetings)\b", lower_text):
        intent = "greeting"
    elif lower_text.strip().endswith("?"):
        intent = "question"
    elif re.search(r"\b(please|could you|would you)\b", lower_text):
        intent = "request"
    elif re.search(r"\b(thank you|thanks)\b", lower_text):
        intent = "thanks"
    else:
        intent = "statement"

    # Tone detection (very naive)
    positive_words = {
        "good",
        "great",
        "fantastic",
        "amazing",
        "nice",
        "love",
        "happy",
    }
    negative_words = {
        "bad",
        "terrible",
        "awful",
        "hate",
        "sad",
        "angry",
    }
    pos_matches = sum(word in lower_text for word in positive_words)
    neg_matches = sum(word in lower_text for word in negative_words)
    if pos_matches > neg_matches:
        tone = "positive"
    elif neg_matches > pos_matches:
        tone = "negative"
    else:
        tone = "neutral"

    # Emotion detection using keywords
    emotion_map = {
        "happy": ["happy", "joy", "excited", "delighted"],
        "sad": ["sad", "unhappy", "sorrow", "depressed"],
        "angry": ["angry", "mad", "furious", "annoyed"],
        "fear": ["fear", "scared", "afraid", "terrified"],
        "surprise": ["surprised", "amazed", "wow"],
    }
    emotion = "neutral"
    for key, keywords in emotion_map.items():
        if any(word in lower_text for word in keywords):
            emotion = key
            break

    return {
        "intent": intent,
        "tone": tone,
        "emotion": emotion,
    }


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        raise SystemExit("Usage: python analyze_text.py 'your text'")
    result = extract_intent_tone_emotion(sys.argv[1])
    print(result)
