# AP1 — IPv4 validation (P0)

## Level check

An IPv4 address has four decimal parts, each between 0 and 255.
Would `192.168.1.256` be valid? Explain before coding.

## One small exercise

Implement `is_valid_ipv4(address)` in `ipv4_validation.py` manually, without
`ipaddress`, socket validation, or regular expressions.

- Input is a string; return a boolean.
- Exactly four nonempty parts separated by literal dots.
- Only ASCII digits 0–9; each part has a value from 0 through 255.
- Reject leading zeros except the single digit `0`.
- Reject whitespace anywhere, signs and Unicode digits; do not strip input.
- Invalid strings return `False`, not a numeric-conversion exception.

These are local contract choices for policies the source asks us to clarify.
`192.168.1.1` and `0.0.0.0` are valid; `01.2.3.4` and `1.2.3` are invalid.

First hint if needed: split on dots and check characters before converting a
part to an integer. A length check can reject oversized parts early.

Run from the `Apple SRE` folder:

```bash
python3 priority_drills/ipv4_validation.py
```

The starter intentionally raises `NotImplementedError`. After your attempt,
explain time/space in terms of input length, including split allocations, and
discuss a changed leading-zero policy.
