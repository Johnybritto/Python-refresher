"""Day 4, P13: summarize request success against an exercise-defined SLO."""

from collections.abc import Iterable
from math import isclose
import math 


def summarize_slo(statuses: Iterable[int], target: float = 0.99) -> dict:


    if target <=0.0 or target >1.0 or math.isnan(target):
        raise ValueError("valid value ")

    total =0 
    successfull = 0 
    for status in statuses:
        total +=1
        if 200<=status<=399:
            successfull += 1 

    failed = total - successfull

    if total == 0:
        return  {
        "total": 0,
        "successful": 0,
        "failed": 0 ,
        "success_rate": None,
        "meets_slo": None
    }

    success_rate = successfull/total
    meets_slo = success_rate >=  target or isclose(target,success_rate)

    return {
        "total": total,
        "successful":successfull,
        "failed": failed,
        "success_rate": success_rate,
        "meets_slo": meets_slo
    }

    """Count 200–399 as successful; return counts, success_rate, and meets_slo."""
    # TODO: Validate the target and consume statuses once using counters.
    raise NotImplementedError("Implement summarize_slo before running checks")


def run_tests() -> None:
    # statuses, target, successful count, expected rate, meets SLO
    cases = [
        ([], 0.99, 0, None, None),
        ([200], 1.0, 1, 1.0, True),
        ([503], 0.99, 0, 0.0, False),
        ([200, 201, 302, 503], 0.75, 3, 0.75, True),
        ([200, 201, 302, 503], 0.8, 3, 0.75, False),
        ([199, 200, 399, 400, 599], 0.4, 2, 0.4, True),
        ([200, 200, 500], 0.67, 2, 2 / 3, False),
        ([100, 404, 500], 0.01, 0, 0.0, False),
    ]
    for statuses, target, successful, rate, meets in cases:
        result = summarize_slo((status for status in statuses), target)
        assert set(result) == {"total", "successful", "failed", "success_rate", "meets_slo"}
        assert result["total"] == len(statuses)
        assert result["successful"] == successful
        assert result["failed"] == len(statuses) - successful
        if rate is None:
            assert result["success_rate"] is None
        else:
            assert isclose(result["success_rate"], rate), f"Wrong rate for {statuses}"
        assert result["meets_slo"] is meets, f"Wrong SLO result for {statuses}, {target}"

    assert summarize_slo([200, 500])["meets_slo"] is False, "Check default target"
    for target in (0, -0.1, 1.1, float("nan"), float("inf"), float("-inf")):
        for statuses in ([], [200]):
            try:
                summarize_slo(iter(statuses), target)
            except ValueError:
                pass
            else:
                raise AssertionError(f"Reject invalid target {target}, even for empty input")

    print("All SLO Summary checks passed")


if __name__ == "__main__":
    run_tests()
