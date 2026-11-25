"""The Tired Dark Lord: A 100-Word Villain Monologue.

Writes one monologue of about 100 words to /output/entry.txt.
Stdlib only, deterministic, no network, no randomness.
"""

import os

MONOLOGUE = (
    "Sit. No\u2014stand, if you must. I have rehearsed this speech three times, "
    "and each time the candles burned lower, so forgive me if I... where was I? "
    "Ah. Yes. The kingdom. Aldermere's wells, you see, I have salted them with "
    "dreamless sleep. By dawn every guard, every priest, every small bright-eyed "
    "hero will lie down mid-sentence, and the throne will simply... be empty. "
    "Waiting. My brother laughed when I first promised it, back when he still "
    "had a throne to laugh from. The tea has gone cold again. "
    "Drink yours before it does the same."
)


def validate(text):
    """Enforce the kit's exact gate before writing.

    /output/entry.txt must be UTF-8 text of 1 to 600 characters, not
    only white space; the brief asks for about 100 words, so we also
    require 95-105 words.
    """
    if not isinstance(text, str) or not text.strip():
        raise ValueError("entry must be non-empty, non-whitespace text")
    text.encode("utf-8")  # raises UnicodeEncodeError if not valid UTF-8
    if not 1 <= len(text) <= 600:
        raise ValueError("entry must be 1-600 characters, got %d" % len(text))
    words = text.split()
    if not 95 <= len(words) <= 105:
        raise ValueError("entry must be 95-105 words, got %d" % len(words))


def main():
    validate(MONOLOGUE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(MONOLOGUE)


if __name__ == "__main__":
    main()
