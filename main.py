"""One-Liner Marathon entry: a single fixed joke, written to /output/entry.txt."""

from pathlib import Path

JOKE = "I bought a standing desk to fix my posture; now I just slouch vertically."


def main() -> None:
    # One fixed line, no randomness: repeated runs are byte-identical.
    # The punchline turns the desk's promise against itself.
    text = JOKE.strip()
    assert 1 <= len(text) <= 280, "entry must be 1-280 characters"
    assert "\n" not in text, "entry must be a single line"
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
