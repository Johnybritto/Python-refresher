# Deferred supplement, P13: SLO Summary

This exercise is deferred after reconciliation with the seven-day source plan.
The active task is [AP1 IPv4 Validation](../priority_drills/AP1_IPV4.md).
The original lesson below is preserved for later practice.

Today starts practical SRE engineering. Work on this one exercise first;
bounded health checks and retries come later. Allow about one hour.

## Level check

If 8 out of 10 requests are successful, what fraction succeeded? Would that
meet a target of 0.9 (90%)?

## One small exercise

Implement `summarize_slo(statuses, target)` in `slo_summary.py`.
An SLO (service-level objective) is a reliability target. For this exercise,
we measure the fraction of successful requests and compare it with the target.
These are exercise-specific rules, not a universal definition of HTTP success.

Contract:

- `statuses` is an iterable of valid integer HTTP status codes from 100 to 599.
  Assume valid status inputs; consume the iterable once without materializing it.
- Count 200–399 as successful. All other status codes count as failed requests.
- `target` is a finite number in `(0, 1]`, defaulting to `0.99`.
  Raise `ValueError` for a target outside that range, including NaN or infinity,
  even when input is empty. Assume a numeric input type.
- Return a dictionary with exactly these keys:
  - `total`: number of requests
  - `successful`: number of successful requests
  - `failed`: number of failed requests
  - `success_rate`: successful / total as a fraction, or `None` for no requests
  - `meets_slo`: whether success_rate >= target, or `None` for no requests
- Compare the unrounded fraction. Equality meets the target.
- Target O(n) time and O(1) extra space.

Example:

```python
summarize_slo([200, 201, 302, 503], target=0.75)
# {
#     "total": 4,
#     "successful": 3,
#     "failed": 1,
#     "success_rate": 0.75,
#     "meets_slo": True,
# }
```

An empty observation period has no measured success rate; it is neither an
automatic pass nor a failure in this exercise.

First hint if needed: count requests and successes during one loop. Calculate
the summary after the loop, handling zero requests before dividing.

Run from the `Apple SRE` folder:

```bash
python3 day04/slo_summary.py
```

The starter intentionally raises `NotImplementedError`. After your attempt,
explain the empty-input choice and the time and space costs. During review,
discuss how you would produce separate summaries for multiple services.
