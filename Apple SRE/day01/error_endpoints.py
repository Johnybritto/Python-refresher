"""Day 1, P03: summarize server errors from JSON log lines."""

import json
from collections.abc import Iterable


def summarize_errors(lines: Iterable[str], k: int) -> dict:
    """Return top error endpoints and the number of invalid input lines.

    A valid line is a JSON object containing a nonempty string ``path`` and an
    integer ``status`` from 100 through 599. Boolean statuses are invalid.

    Target complexity:
    - O(C + m log m) time for C input characters and m error endpoints
    - O(m) count storage, apart from the current parsed line
    """

    error_counts = {}
    invalid_lines = 0

    for line in lines:
        try:
            record = json.loads(line)
        except json.JSONDecodeError:
            invalid_lines += 1
            continue

        if not isinstance(record, dict):
            invalid_lines += 1
            continue

        path = record.get("path")
        status = record.get("status")

        invalid_record = (
            not isinstance(path, str)
            or path == ""
            or isinstance(status, bool)
            or not isinstance(status, int)
            or not 100 <= status <= 599
        )

        if invalid_record:
            invalid_lines += 1
            continue

        if 500 <= status <= 599:
            error_counts[path] = error_counts.get(path, 0) + 1

    sorted_errors = sorted(
        error_counts.items(),
        key=lambda item: (-item[1], item[0]),
    )
    top_errors = sorted_errors[:k] if k > 0 else []

    return {
        "top": top_errors,
        "invalid_lines": invalid_lines,
    }


def run_tests() -> None:
    """Run examples plus boundary and malformed-input cases."""
    lines = [
        '{"path":"/login","status":503}',
        '{"path":"/health","status":200}',
        '{"path":"/login","status":500}',
        '{"path":"/search","status":502}',
        "broken-json",
    ]
    assert summarize_errors(lines, 2) == {
        "top": [("/login", 2), ("/search", 1)],
        "invalid_lines": 1,
    }

    assert summarize_errors(iter(()), 3) == {"top": [], "invalid_lines": 0}
    assert summarize_errors(['{"path":"/health","status":200}'], 3) == {
        "top": [],
        "invalid_lines": 0,
    }

    tied = [
        '{"path":"/z","status":500}',
        '{"path":"/a","status":501}',
        '{"path":"/m","status":502}',
    ]
    assert summarize_errors(tied, 10)["top"] == [
        ("/a", 1),
        ("/m", 1),
        ("/z", 1),
    ]

    invalid = [
        "",
        "[]",
        '{"status":500}',
        '{"path":"","status":500}',
        '{"path":"/api"}',
        '{"path":"/api","status":true}',
        '{"path":"/api","status":99}',
        '{"path":"/api","status":600}',
    ]
    assert summarize_errors(invalid, 5) == {"top": [], "invalid_lines": 8}

    generator = (line for line in ["bad", '{"path":"/api","status":500}'])
    assert summarize_errors(generator, 0) == {"top": [], "invalid_lines": 1}
    assert summarize_errors(['{"path":"/api","status":500}'], -2) == {
        "top": [],
        "invalid_lines": 0,
    }

    print("All Error Endpoint tests passed")


if __name__ == "__main__":
    run_tests()
