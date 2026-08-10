#!/usr/bin/env python3
"""Move fully-closed items out of lexor's tasks.md into tasks/done-archive.md.

Adapted from kart-medulla's tasks/archive_done.py. Difference from that repo: lexor's
board nests sub-questions under a single top-level bullet (indented `- [ ]` / `- [x]`
lines under a parent bullet) rather than using `###` cluster headings. So the unit that
moves or stays is a *top-level bullet plus its whole indented subtree*, not a heading
section:

  * a top-level bullet moves to the archive only if it AND every checkbox nested under
    it are `[x]` -- if any nested sub-question is still `[ ]` (or `[~]`), the whole
    bullet (parent text plus all children, closed and open alike) stays on the board,
    because the closed children record what's already settled and the open child
    needs that context.
  * a top-level bullet with no children just needs its own checkbox to be `[x]`.
"""
import re, sys

TASKS = "/Users/rubenayla/repos/lexor/tasks.md"
ARCHIVE = "/Users/rubenayla/repos/lexor/tasks/done-archive.md"
lines = open(TASKS).read().split("\n")

CHECKBOX = re.compile(r"^(\s*)- \[(.)\]")


def top_block_at(src, i):
    """Top-level bullet at src[i] (indent 0) plus everything indented under it."""
    block = [src[i]]
    j = i + 1
    while j < len(src):
        nxt = src[j]
        if nxt == "":
            if j + 1 < len(src) and re.match(r"^\s+\S", src[j + 1]):
                block.append(nxt)
                j += 1
                continue
            break
        if re.match(r"^\s+\S", nxt):
            block.append(nxt)
            j += 1
            continue
        break
    return block, j


def fully_closed(block):
    for l in block:
        m = CHECKBOX.match(l)
        if m and m.group(2) != "x":
            return False
    return True


kept, archived = [], []
i = 0
while i < len(lines):
    l = lines[i]
    m = CHECKBOX.match(l)
    if m and m.group(1) == "":  # top-level bullet
        block, i = top_block_at(lines, i)
        if fully_closed(block):
            archived.append(block)
        else:
            kept += block
        continue
    kept.append(l)
    i += 1

print(f"top-level bullets archived : {len(archived)}")
n_lines_archived = sum(len(b) for b in archived)
print(f"total lines archived       : {n_lines_archived}")

if "--apply" not in sys.argv:
    print("\n(dry run -- pass --apply to write)")
    for b in archived:
        print(f"  {b[0][:100]}")
    sys.exit(0)

header = [
    "<!-- reference — read only when you need the history of a shipped item -->",
    "# Done archive — completed work items",
    "",
    "Closed items moved out of the root `tasks.md` on 2026-08-10, following the same",
    "convention as the partle and kart-medulla repos. Nothing here is actionable: the root",
    "board carries only live work, while the reasoning behind resolved design questions",
    "stays findable.",
    "",
    "The board is `tasks.md` at the repo root — the only task board in this repo.",
    "",
    "A top-level bullet only moves here once it AND every sub-question nested under it are",
    "closed. A resolved top-level item that still has an open sub-question (e.g. a design",
    "round that closed the framework but left a follow-up parked) stays on the board whole,",
    "closed children included, so the open child keeps the context for what was already",
    "settled.",
    "",
    "## Closed design decisions",
    "",
]

out = header[:]
for b in archived:
    out += b + [""]

with open(ARCHIVE, "w") as f:
    f.write("\n".join(out).rstrip() + "\n")

with open(TASKS, "w") as f:
    f.write("\n".join(kept).rstrip() + "\n")
print("\nwritten.")
