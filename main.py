#!/usr/bin/env python3
# Entry for make-the-ai-judge-feel-curious-20261122-2311 — The Lighthouse at 3 A.M.
"""Write the entry text to $MAKEFUN_OUTPUT_DIR/entry.txt (or /output/entry.txt). No deps, no network, deterministic."""
import os
TEXT = "Last night, at 3 a.m., a lighthouse that stood dark for forty years switched itself on - and off again before anyone could reach it. The logbook's last page, dated yesterday, is in handwriting no one at the station recognises."
def main():
    out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8", newline="\n") as f:
        f.write(TEXT)
if __name__ == "__main__":
    main()
