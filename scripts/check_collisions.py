#!/usr/bin/env python3
"""Check lexicon.yaml for root-form collisions and basic shape violations.

Run from repo root:
    python3 scripts/check_collisions.py

Exit code 0 if clean, 1 if any collision or shape violation is found.

Whitelisted overloads (one root, one concept, two syntactic contexts) must be
listed below. Currently:
    - "sam": comparison "=" and identity copula (decisions.md 2026-05-16).
"""
from __future__ import annotations

import re
import sys
from collections import defaultdict
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.stderr.write("PyYAML missing. Install: pip install pyyaml\n")
    sys.exit(2)

LEXICON = Path(__file__).resolve().parent.parent / "lexicon.yaml"

# Phoneme inventory (per phonetics.md). Update if the inventory changes.
VOWELS = set("aeiouyc")
CONSONANTS = set("bcdfghjklmnpqrstvwxz") | {"ch"}

# Multi-char consonants — order matters for longest-match parsing.
MULTI_CONS = ["ch"]

# Roots allowed to appear more than once because they're the same concept
# used in two syntactic contexts (overload formally locked in decisions.md).
ALLOWED_OVERLOADS = {"sam"}


def split_phonemes(s: str) -> list[str]:
    """Greedy left-to-right phoneme split using MULTI_CONS first."""
    out: list[str] = []
    i = 0
    while i < len(s):
        matched = False
        for mc in MULTI_CONS:
            if s.startswith(mc, i):
                out.append(mc)
                i += len(mc)
                matched = True
                break
        if not matched:
            out.append(s[i])
            i += 1
    return out


def classify_shape(root: str) -> str:
    """Return a shape label: V, CV, CVC, CCV, CVCC, etc., or 'special'."""
    if root.endswith("-"):
        return "prefix"
    if root == "":
        return "empty"
    phones = split_phonemes(root)
    pattern = []
    for p in phones:
        if p in VOWELS:
            pattern.append("V")
        elif p in CONSONANTS:
            pattern.append("C")
        else:
            return f"special({root})"
    return "".join(pattern)


def main() -> int:
    if not LEXICON.exists():
        sys.stderr.write(f"Missing lexicon: {LEXICON}\n")
        return 2

    data = yaml.safe_load(LEXICON.read_text())
    if not isinstance(data, list):
        sys.stderr.write("lexicon.yaml must be a top-level list.\n")
        return 2

    errors: list[str] = []
    warnings: list[str] = []
    by_root: dict[str, list[dict]] = defaultdict(list)

    # Closed-class shapes are hand-chosen and locked in decisions.md — they are
    # allowed to deviate from the CVC default (e.g. `est`, `ant`, `imp`, `is`).
    # Only open-class kinds (verb, noun, adj) are enforced to CVC.
    SHAPE_ALLOW: dict[str, set[str]] = {
        "verb": {"CVC"},
        "noun": {"CVC"},
        "adj": {"CVC"},
    }
    CLOSED_CLASS = {
        "pronoun", "digit", "marker", "coordinator", "quantifier",
        "copula", "preposition", "time_unit",
    }

    REQUIRED = {"root", "kind", "concept"}

    for idx, entry in enumerate(data):
        if not isinstance(entry, dict):
            errors.append(f"entry {idx}: not a mapping")
            continue
        missing = REQUIRED - entry.keys()
        if missing:
            errors.append(f"entry {idx}: missing required fields {sorted(missing)}")
            continue

        root = entry["root"]
        kind = entry["kind"]
        by_root[root].append(entry)

        shape = classify_shape(root)
        if kind in SHAPE_ALLOW and shape not in SHAPE_ALLOW[kind]:
            warnings.append(
                f"shape mismatch: {root!r} ({kind}) has shape {shape}, "
                f"expected one of {sorted(SHAPE_ALLOW[kind])}"
            )
        elif kind not in CLOSED_CLASS and kind not in SHAPE_ALLOW:
            warnings.append(f"unknown kind {kind!r} for entry {idx} ({root!r})")

    # Collision pass
    for root, entries in by_root.items():
        if len(entries) > 1 and root not in ALLOWED_OVERLOADS:
            concepts = [e.get("concept", "?") for e in entries]
            errors.append(
                f"collision: root {root!r} used by {len(entries)} entries: {concepts}"
            )

    # CVC fingerprint pass: warn if two distinct CVC roots only differ in voicing
    # or are otherwise minimal-pair confusable. Skip for now — placeholder.

    # Report
    if warnings:
        print("Warnings:")
        for w in warnings:
            print(f"  - {w}")
        print()

    if errors:
        print("Errors:")
        for e in errors:
            print(f"  - {e}")
        print()
        print(f"FAIL: {len(errors)} error(s), {len(warnings)} warning(s)")
        return 1

    print(f"OK: {len(data)} entries, {len(by_root)} unique roots, "
          f"{len(warnings)} warning(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
