#!/usr/bin/env python3
"""One Emoji, One Smile.

Picks the single emoji most likely to make a stranger smile, scores ten
fresh candidates on five criteria, and writes the winner — exactly one
emoji, no words, no newline — to entry.txt in the output directory.

The competition gate: /output/entry.txt must be UTF-8 text of 1 to 8
characters, not only white space. The judge shows two emojis at a time
and picks the warmer, weighing warmth at first glance first, then
universality, then whether the emoji feels chosen rather than the
default smiley, then whether it reads right coming from a stranger
(no intimacy, sarcasm or flirtation).

Scoring (each 0-10): original (chosen, not the first smiley that comes
to mind), warm (kind, friendly, gently funny at first glance), on-theme
(a stranger reads it as a smile), exact RULES format (exactly one
emoji, 1-8 chars), no extra words (nothing but the emoji itself).
Highest total wins; ties go to the fewer UTF-8 bytes. Deterministic,
standard library only, no network, no randomness, no clock.
"""

import os
import unicodedata

MAX_CHARS = 8

# (emoji, name, original, warm, on-theme)
# Scores reasoned against the judge's brief, most important first:
# - hugging face wins on "chosen": open arms plus a smile is a warm
#   welcome that no default smiley offers, yet anyone reads it instantly,
#   and a virtual hug from a stranger is friendly, not intimate.
# - the plain smileys score high on warmth but low on "chosen": they are
#   the first smileys that come to mind, so any picked emoji beats them.
# - smiling face with hearts loses on "right for a stranger": hearts
#   around a face can read as flirtation from someone unknown.
# - heart hands and the sunflower are warm but are not smiles, so they
#   lose to any emoji that plainly aims to warm a stranger with a smile.
# - face holding back tears is moving, not smiling, and tears from a
#   stranger can land wrong.
CANDIDATES = [
    ("\U0001F642", "slightly smiling face", 4, 6, 8),
    ("\U0001F60A", "smiling face with smiling eyes", 3, 9, 9),
    ("\U0001F604", "grinning face with smiling eyes", 5, 8, 9),
    ("\U0001F601", "beaming face with smiling eyes", 5, 8, 9),
    ("\U0001F917", "hugging face", 9, 10, 9),
    ("\U0001F970", "smiling face with hearts", 6, 8, 7),
    ("\U0001FAF6", "heart hands", 8, 7, 6),
    ("\U0001F33B", "sunflower", 8, 6, 5),
    ("\U0001F31E", "sun with face", 6, 6, 6),
    ("\U0001F979", "face holding back tears", 8, 5, 4),
]


def is_single_emoji(text):
    """True when text is exactly one emoji codepoint, nothing else."""
    if len(text) != 1:
        return False
    if text.isspace():
        return False
    return unicodedata.category(text) == "So"


def format_score(text):
    """10 when the text is exactly one emoji inside the 1-8 char gate."""
    if not text or text.isspace():
        return 0
    if len(text) > MAX_CHARS:
        return 0
    return 10 if is_single_emoji(text) else 0


def no_words_score(text):
    """10 when the text carries no letters, spaces or punctuation at all."""
    if not text:
        return 0
    if any(ch.isalnum() or ch.isspace() or unicodedata.category(ch)[0] == "P"
           for ch in text):
        return 0
    return 10


def score(candidate):
    emoji, _name, original, warm, theme = candidate
    return original + warm + theme + format_score(emoji) + no_words_score(emoji)


def validate_entry(text):
    """Re-check the winner against the competition gate before writing.

    The sealed scorer accepts UTF-8 text of 1 to 8 characters, not only
    white space; this entry must be exactly one emoji and nothing else.
    """
    if not isinstance(text, str) or not text:
        raise ValueError("entry is empty")
    if not text.strip():
        raise ValueError("entry is only white space")
    if len(text) > MAX_CHARS:
        raise ValueError(f"entry is {len(text)} chars, over the {MAX_CHARS} gate")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must not contain a newline")
    if not is_single_emoji(text):
        raise ValueError("entry is not exactly one emoji")
    raw = text.encode("utf-8")
    if raw.decode("utf-8") != text:
        raise ValueError("entry does not round-trip as UTF-8")
    return text


def pick_best():
    ranked = sorted(
        CANDIDATES,
        key=lambda c: (score(c), -len(c[0].encode("utf-8"))),
        reverse=True,
    )
    best = ranked[0]
    if score(best) <= 0 or format_score(best[0]) != 10:
        raise ValueError("no candidate passes the exact-one-emoji gate")
    return best, ranked


def main():
    (emoji, name, _o, _w, _t), ranked = pick_best()
    emoji = validate_entry(emoji)
    for candidate in ranked:
        print(f"{candidate[0]} {candidate[1]}: {score(candidate)}/50")
    print(f"winner: {emoji} ({name})")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(emoji)
    print(f"wrote {len(emoji)} char to {path}")


if __name__ == "__main__":
    main()
