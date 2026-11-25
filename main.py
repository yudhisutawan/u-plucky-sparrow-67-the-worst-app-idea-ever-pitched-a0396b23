# SPDX-License-Identifier: MIT
"""Entry for make.fun: The Worst App Idea Ever Pitched.

Writes one sentence (214 characters) pitching the worst, most useless
app imaginable to /output/entry.txt. Standard library only.
"""

import os

ENTRY = (
    "Voicemail Ballet is an app that converts every voicemail you receive "
    "into step-by-step interpretive dance instructions, so you can finally "
    "experience your landlord's eviction notice as a moving piece of modern art."
)


def main() -> None:
    # Competition cap: one sentence, at most 280 characters.
    assert len(ENTRY) <= 280, f"entry is {len(ENTRY)} chars, over the 280 cap"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
