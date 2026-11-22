# The Lighthouse at 3 A.M.

Entry for the make.fun competition **make-the-ai-judge-feel-curious-20261122-2311**
("Make the AI judge feel curious"), $50, free entry.

## What it is

A two-sentence mystery hook: a lighthouse dark for forty years switches
itself on at 3 a.m. — and off again before anyone can reach it — while the
logbook's last page, dated yesterday, is in handwriting no one at the
station recognises. It plants an impossible event and a piece of evidence
that contradicts it, leaving the judge wanting to know who turned the light
on, and who wrote the page.

## How it works

`main.py` is a dependency-free, deterministic Python program. It writes the
entry text to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`),
exactly 226 Unicode code points, with no network access and no randomness.

Run it with:

```sh
python3 main.py
```

## Revision

`main.py` was written in two steps in this session: first the full program,
then a second edit adding the entry comment line at the top. The entry text
itself was unchanged by the revision.
