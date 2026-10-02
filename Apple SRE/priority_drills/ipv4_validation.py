"""AP1 (P0): manually validate IPv4 using AP1_IPV4.md's contract."""


def is_valid_ipv4(address: str) -> bool:

 # split and check 4 parts are there or not 
    chunks = address.split('.')
    if len(chunks) != 4:
        return False

    for chunk in chunks:

        #check each part is digit or not 

        if not chunk.isdigit():
            return False

        # check each char in chunk is number or not 

        for char in chunk:
            if char not in '0123456789':
                return False

        #check each part is not have a leading 0  eacmple 10.1.01.1

        if len(chunk) > 1 and chunk[0] == "0":
            return False

      # chek whether they fall in the octet 
        value = int(chunk)
        if value <0 or value >255:
            return False

    return True
        
    """Accept four ASCII decimal octets; reject whitespace and leading zeros."""
    # TODO: Attempt manually before asking for stronger hints.
    raise NotImplementedError("Implement is_valid_ipv4 before running checks")


def run_tests() -> None:
    valid = ["192.168.1.1", "0.0.0.0", "255.255.255.255", "1.2.3.4"]
    invalid = [
        "", "1.2.3", "1.2.3.4.5", "1..3.4", ".1.2.3", "1.2.3.",
        "256.1.2.3", "1.2.3.-1", "1.2.3.+1", "01.2.3.4", "00.0.0.0",
        " 1.2.3.4", "1.2.3.4 ", "1.2. 3.4", "a.2.3.4",
        "١.2.3.4", "１.2.3.4", "1.2.3.9999",
    ]
    for address in valid:
        assert is_valid_ipv4(address) is True, f"Expected valid: {address!r}"
    for address in invalid:
        assert is_valid_ipv4(address) is False, f"Expected invalid: {address!r}"
    print("All IPv4 Validation checks passed")


if __name__ == "__main__":
    run_tests()
