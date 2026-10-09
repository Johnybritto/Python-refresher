"""R23-C01 — Normalize, count, and rank strings.

Problem statement
-----------------
Given an iterable containing arbitrary values, count equivalent strings. A
valid value is a string that remains non-empty after removing surrounding
whitespace. Normalize every valid string with ``strip().lower()`` before
counting it. Skip invalid values (non-strings or blank strings) and report how
many were skipped.

Return a dictionary with:

* ``counts``: normalized strings and their counts, ordered by descending count
  and then alphabetically for equal counts.
* ``top``: at most ``top_k`` ``(string, count)`` pairs in the same order.
* ``invalid_items``: number of skipped values.

``top_k=None`` means return every ranked item. An integer ``top_k <= 0`` means
return an empty ``top`` list. A non-integer ``top_k`` must raise ``TypeError``.
Consume the input once and do not modify it.

Sample input
------------
    ["ABC ", "XYZ ", "TYP", "ABC ", " ABC", " TYP "]

Sample output
-------------
    {
        "counts": {"abc": 3, "typ": 2, "xyz": 1},
        "top": [("abc", 3), ("typ", 2), ("xyz", 1)],
        "invalid_items": 0,
    }

In plain language
-----------------
The program accepts strings from either a list/generator or a file. It cleans
and counts valid values, ranks the counts from highest to lowest (with
alphabetical tie-breaking), and optionally returns only the first ``top_k``
ranked results.

File variant
------------
``normalize_and_count_file`` reads a UTF-8 file one line at a time and applies
the same rules. File errors should propagate to the caller.
"""

from collections.abc import Iterable
from pathlib import Path


def normalize_and_count(
    items: Iterable[object], top_k: int | None = None
) -> dict[str, object]:

    # Keep the number of values that are not usable strings.
    invalid_items=0
    # Store each normalized string and how many times it appears.
    result = {}

    # ``items`` can be a list, generator, or an opened file (one line at a time).
    for i in items:
        # Reject non-string values before using string methods such as strip().
        if not isinstance(i, str):
            invalid_items +=1
            continue

        # Remove surrounding whitespace and make equivalent letter cases match.
        b=i.strip().lower()
        # A blank string after cleanup is invalid too.
        if not b:
            invalid_items +=1
            continue

        # Increment the count for this normalized value.
        if b in result:
            result[b] +=1
        else:
            result[b] = 1

    # Sort by count descending; for tied counts, sort the string alphabetically.
    out = dict(sorted(result.items() , key=lambda x :(-x[1], x[0])))

    # Only None or an integer is allowed as the requested number of top results.
    if top_k is not None and not isinstance(top_k , int):
        raise TypeError ("top must be int ")

    # No limit means every ranked result; a number means take that many from front.
    if top_k is None:
        top = list(out.items())
    else:
        # max(..., 0) makes zero and negative limits return an empty list.
        top = list(out.items())[:max(top_k,0)]

    # Return both all counts and the optional top-K view, plus invalid-item count.
    return {
        "counts": out,
        "top": top,
        "invalid_items": invalid_items
    }





    """Return normalized counts, a deterministic top list and invalid count."""
    # TODO: Validate top_k, consume items once, and count valid normalized strings.
    # TODO: Sort by descending count then alphabetical normalized value.
    raise NotImplementedError("Implement R23-C01 before running checks")


def normalize_and_count_file(
    path: str | Path, top_k: int | None = None
) -> dict[str, object]:

    # Open the supplied path for reading. The file object yields one line at a time.
        with open(path , "r", encoding="UTF-8") as file:
            # Reuse the same counting logic instead of duplicating it for files.
            return normalize_and_count(file, top_k)



def run_tests() -> None:
    expected = {
        "counts": {"abc": 3, "typ": 2, "xyz": 1},
        "top": [("abc", 3), ("typ", 2), ("xyz", 1)],
        "invalid_items": 0,
    }
    assert normalize_and_count(
        (item for item in ["ABC ", "XYZ ", "TYP", "ABC ", " ABC", " TYP "])
    ) == expected
    assert normalize_and_count([" B ", "a", "A", "", None, " b"]) == {
        "counts": {"a": 2, "b": 2},
        "top": [("a", 2), ("b", 2)],
        "invalid_items": 2,
    }
    assert normalize_and_count([], top_k=3) == {
        "counts": {}, "top": [], "invalid_items": 0
    }
    assert normalize_and_count(["x", "y", "x", "z"], top_k=2)["top"] == [
        ("x", 2), ("y", 1)
    ]
    assert normalize_and_count(["x"], top_k=0)["top"] == []
    for bad_top_k in ("2", 1.5):
        try:
            normalize_and_count(["x"], top_k=bad_top_k)  # type: ignore[arg-type]
        except TypeError:
            pass
        else:
            raise AssertionError("Non-integer top_k must raise TypeError")

    from tempfile import TemporaryDirectory

    with TemporaryDirectory() as directory:
        path = Path(directory) / "items.txt"
        path.write_text("Alpha\n beta \n\nALPHA\n", encoding="utf-8")
        assert normalize_and_count_file(path, top_k=1) == {
            "counts": {"alpha": 2, "beta": 1},
            "top": [("alpha", 2)],
            "invalid_items": 1,
        }
    print("All R23-C01 checks passed")


if __name__ == "__main__":
    run_tests()
