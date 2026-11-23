"""Warning label for humans: one line, big laugh.

The whole entry is a single warning label in the voice of a printed
safety label: what this human "runs on", listed like fuel specs, with
the joke turning in the last few words — the firm belief that tomorrow,
finally, the exercising starts. Nothing else is needed here — the
script validates the line and drops it into /output/entry.txt.
"""

from pathlib import Path

# The label itself: 138 characters, in three fragments joined at write
# time by assemble_label(). The setup reads like a real spec sheet
# ("runs on three hours of sleep, one strong coffee") so the punch
# lands as recognition: everyone knows a human powered by sleep debt,
# caffeine, and a tomorrow that never comes. The turn arrives in the
# last few words — "finally start exercising" — the one promise every
# human makes to themselves and breaks by breakfast.
OPENING = "WARNING: This human runs on "
FUEL = "three hours of sleep, one strong coffee, "
CLOSING = (
    "and the firm belief that tomorrow they will finally "
    "start exercising."
)


def assemble_label() -> str:
    """Join the label fragments into the single-line warning."""
    return OPENING + FUEL + CLOSING


OUTPUT_DIR = Path("/output")
OUTPUT_FILE = OUTPUT_DIR / "entry.txt"
MIN_CHARS = 1
MAX_CHARS = 160


def validate(line: str) -> str:
    """Strip and sanity-check the label; raise ValueError on bad input."""
    text = line.strip()
    if not MIN_CHARS <= len(text) <= MAX_CHARS:
        raise ValueError(
            f"label must be {MIN_CHARS}-{MAX_CHARS} chars, got {len(text)}"
        )
    if not text:
        raise ValueError("label must not be whitespace-only")
    if "\n" in text:
        raise ValueError("label must be a single line")
    return text


def main() -> None:
    text = validate(assemble_label())
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text(text, encoding="utf-8")
    print(text)
    print(f"Wrote {len(text)} chars to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
