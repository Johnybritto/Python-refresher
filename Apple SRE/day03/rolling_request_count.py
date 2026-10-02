"""Day 3, P10: count requests in a moving time window."""

from collections import deque
from collections.abc import Iterable


def rolling_request_counts(timestamps: Iterable[int], window: int) -> list[int]:


    if window <=0:
        raise ValueError(" window size should be positive")

    counts = [] 
    recent_request = deque()



    for i in timestamps:
        recent_request.append(i)

        while recent_request and recent_request[0] <= i - window:
            recent_request.popleft()

        counts.append(len(recent_request))

    print(counts)

    return counts
   
    """Count arrivals seen so far in (t - window, t]; reject nonpositive windows."""
    # TODO: Process timestamps once, using a deque for recent requests.
    raise NotImplementedError("Implement rolling_request_counts before running checks")


def run_tests() -> None:
    cases = [
        ([], 3, []),
        ([5], 3, [1]),
        ([1, 2, 3, 7], 3, [1, 2, 3, 1]),
        ([1, 4], 3, [1, 1]),
        ([1, 3], 3, [1, 2]),
        ([5, 5, 5], 3, [1, 2, 3]),
        ([0, 1, 2, 3], 2, [1, 2, 2, 2]),
        ([1, 1, 2], 1, [1, 2, 1]),
        ([1, 2, 3, 100], 5, [1, 2, 3, 1]),
    ]
    for timestamps, window, expected in cases:
        # Generators ensure the function supports a single-pass input.
        result = rolling_request_counts((t for t in timestamps), window)
        assert isinstance(result, list), "Return a list of counts"
        assert result == expected, (
            f"For {timestamps}, window={window}: expected {expected}, got {result}"
        )

    for window in (0, -1):
        for timestamps in ([], [1]):
            try:
                rolling_request_counts(iter(timestamps), window)
            except ValueError:
                pass
            else:
                raise AssertionError("Reject nonpositive windows, even with empty input")

    print("All Rolling Request Count checks passed")


if __name__ == "__main__":
    run_tests()
