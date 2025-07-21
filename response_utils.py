# Simple text generation utilities

def generate_response(character_profile, parsed_input):
    """Return a natural language response string based on character traits,
    relationship status and the parsed intent.

    Parameters
    ----------
    character_profile : dict
        Dictionary containing keys like ``name``, ``traits`` (list of strings)
        and ``relationship`` (``friendly``, ``neutral`` or ``hostile``).
    parsed_input : dict
        Parsed representation of user input containing an ``intent`` value.

    Returns
    -------
    str
        Generated response sentence.
    """
    name = character_profile.get("name", "")
    traits = character_profile.get("traits", [])
    if isinstance(traits, str):
        traits = [traits]
    relationship = character_profile.get("relationship", "neutral")
    intent = parsed_input.get("intent", "unknown")

    def apply_tone(base):
        if relationship == "friendly":
            return f"{base} :)"
        if relationship == "hostile":
            return f"{base}".replace(".", "!")
        return base

    if intent == "greet":
        response = f"Hello, I'm {name}." if name else "Hello."
    elif intent == "farewell":
        response = "Goodbye."
    elif intent == "compliment":
        response = "Thank you!"
    elif intent == "insult":
        if relationship == "hostile":
            response = "Watch your tongue."
        else:
            response = "That's not very nice."
    elif intent == "question":
        response = "I'm thinking about that." if "thoughtful" in traits else "Let me see."
    else:
        response = "I'm not sure how to respond to that."

    # Modify response based on traits
    if "sarcastic" in traits:
        response = "Oh, really? " + response
    if "formal" in traits:
        response = response.replace("I'm", "I am")
    response = apply_tone(response)
    return response
