"""One-line joke about working beside AI coding agents.

Writes the joke to /output/entry.txt. Standard library only, no network.
"""

import os

JOKE = "I asked the agent for a one-line fix; it changed fourteen files and called it minimal."

# The gate requires 1 to 280 Unicode code points; refuse to write an
# over-long text rather than submit an entry the scorer would void.
MAX_CHARS = 280


def main() -> None:
    if not 1 <= len(JOKE) <= MAX_CHARS:
        raise ValueError("joke must be 1 to 280 characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
