"""Write one short out-of-office reply for make.fun bounty d2a8974d."""

import os
import sys

TEXT = (
    "On leave until the 14th. A wasp has built a nest in the mailbox and I respect her. "
    "All my mail is being held at the post office, and by the wasp."
)


def main() -> None:
    assert 1 <= len(TEXT) <= 280, "entry must be between 1 and 280 characters"
    out_dir = (
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
        or "/output"
    )
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "wb") as handle:
        handle.write(TEXT.encode("utf-8"))
    print(len(TEXT), file=sys.stderr)


if __name__ == "__main__":
    main()
