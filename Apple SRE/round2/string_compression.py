"""R23-C03 — String compression.

Problem statement
-----------------
Compress consecutive repeated characters. Keep a single character unchanged;
after two or more consecutive copies, append the count immediately after that
character. Do not combine matching characters separated by a different one.

Implement two versions:

* ``compress(text)`` returns a new compressed string.
* ``compress_chars(chars)`` modifies a list of single-character strings in
  place and returns the new compressed length. Only the first returned-length
  positions need to contain the compressed result.

Sample input and output
-----------------------
    compress("aaabbc") == "a3b2c"
    compress("aabcccccaaa") == "a2bc5a3"
    compress("") == ""

For the in-place version:

    chars = ["a", "a", "b", "b", "c", "c", "c"]
    length = compress_chars(chars)
    # length == 6
    # chars[:length] == ["a", "2", "b", "2", "c", "3"]

Important details
-----------------
Groups with counts above nine must write every digit: twelve ``"a"`` values
become ``["a", "1", "2"]``. An empty list/string is valid. Target time is
O(n); the returned-string version may use O(n) output storage, while the
character-list version should use O(1) extra working space apart from digit
conversion.
"""


def compress(text: str) -> str:

    # ``read`` marks the first character of the next consecutive group.
    read = 0 
    # ``write`` accumulates the compressed text that this version returns.
    write = ""

    while read < len(text):
        # Remember the character whose consecutive group we are processing.
        char = text[read]
        # Count how many times this character occurs consecutively.
        count = 0 

        # Move read across this whole group, stopping at a new character or the end.
        while read < len(text) and text[read] == char:
            count +=1
            read +=1

        # Every group contributes its character once to the compressed result.
        write = write+str(char)

        # A one-character group stays as just the character; repeated groups add count.
        if count > 1 :
            write = write +str(count)

    # Return the newly built compressed string after every group is processed.
    return write

    
    """Return run-length compression of text."""
    raise NotImplementedError("Implement R23-C03 before running checks")


def compress_chars(chars: list[str]) -> int:

# for list we need to do inplace which means we cannot create a newlist 
    read = 0
    write = 0 

    while read < len(chars):
        char = chars[read]
        count = 0 

        while read < len(chars) and chars[read] == char:
            count +=1
            read +=1

        chars[write] = char
        write +=1

        if count >1:
            for c in str(count):
                chars[write] = c
                write +=1

    return write 
    """Compress chars in place and return the compressed length."""
    raise NotImplementedError("Implement R23-C03 before running checks")


def run_tests() -> None:
    cases = {
        "": "",
        "a": "a",
        "abc": "abc",
        "aaabbc": "a3b2c",
        "aabcccccaaa": "a2bc5a3",
        "aaaaaaaaaaaa": "a12",
        "aabba": "a2b2a",
    }
    for text, expected in cases.items():
        assert compress(text) == expected, f"For {text!r}: expected {expected!r}"

    char_cases = [
        ([], [], 0),
        (["a"], ["a"], 1),
        (["a", "a", "b", "b", "c", "c", "c"], ["a", "2", "b", "2", "c", "3"], 6),
        (["a"] * 12, ["a", "1", "2"], 3),
        (["a", "b", "b", "a"], ["a", "b", "2", "a"], 4),
    ]
    for chars, expected_prefix, expected_length in char_cases:
        original = chars
        length = compress_chars(chars)
        assert chars is original, "Modify the supplied list rather than replacing it"
        assert length == expected_length, f"Wrong length for {original}"
        assert chars[:length] == expected_prefix, f"Wrong prefix for {original}"
    print("All R23-C03 checks passed")


if __name__ == "__main__":
    run_tests()
