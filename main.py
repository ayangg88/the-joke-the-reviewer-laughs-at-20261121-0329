"""One-line joke about working beside AI coding agents.

Writes the joke to /output/entry.txt. Standard library only, no network.
"""

import os

JOKE = "I asked the agent for a one-line fix; it changed fourteen files and called it minimal."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
