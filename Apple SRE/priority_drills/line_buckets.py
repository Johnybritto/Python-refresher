"""AP2 (P0): distribute lines round-robin into evenly sized buckets."""

from collections.abc import Iterable


def split_lines(lines: Iterable[str], bucket_count: int) -> list[list[str]]:
    """Return independent buckets; preserve strings and reject nonpositive counts."""
    if bucket_count <= 0:
        raise ValueError("bucket_count must be greater than 0")
    #checking the bucket count it should 0 or more 


     # list comprenhension to generate the empty buckets based on the bucket counts 

    buckets = [[] for _ in range(bucket_count)]

     # setting total lines to 0 
    total_lines = 0
    for line in lines:

        # eg if bucket_count is 3 then 1 %3 would be 1  
        bucket_index = total_lines % bucket_count
        buckets[bucket_index].append(line)
        total_lines += 1
    return buckets


def run_tests() -> None:
    cases = [
        ([], 3, [[], [], []]),
        (["A"], 1, [["A"]]),
        (["A", "B"], 4, [["A"], ["B"], [], []]),
        (["A", "B", "C"], 1, [["A", "B", "C"]]),
        (["A", "B", "C", "D"], 2, [["A", "C"], ["B", "D"]]),
        (["A", "B", "C", "D", "E", "F", "G"], 3,
         [["A", "D", "G"], ["B", "E"], ["C", "F"]]),
        (["same", "same", "same"], 2, [["same", "same"], ["same"]]),
        ([" A", "", "  ", "last"], 2, [[" A", "  "], ["", "last"]]),
    ]
    for lines, count, expected in cases:
        result = split_lines((line for line in lines), count)
        assert result == expected, f"For {lines}, {count}: got {result}"
        assert len({id(bucket) for bucket in result}) == count, "Use independent buckets"

    from io import StringIO
    with StringIO("first\n\nlast") as file:
        assert split_lines(file, 2) == [["first\n", "last"], ["\n"]]

    for count in (0, -1):
        for lines in ([], ["A"]):
            try:
                split_lines(iter(lines), count)
            except ValueError:
                pass
            else:
                raise AssertionError("Reject nonpositive counts, even for empty input")
    print("All Line Buckets checks passed")


if __name__ == "__main__":
    run_tests()


