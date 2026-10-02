"""Day 3, P11: merge overlapping closed intervals without changing the input."""


def merge_intervals(intervals: list[tuple[int, int]]) -> list[tuple[int, int]]:


    #intervals.sort(key=lambda x: x[0])

    interval = sorted(intervals, key=lambda x :x[0])

    merged_list=[]

    for i in interval:
        if not merged_list or merged_list[-1][1] < i[0]:
            merged_list.append(i)
        else:
            #the below code will work in the input is list.. example look at leet code 
            #def merge(self, intervals: list[list[int]]) -> list[list[int]]:
            #but in our case the input is tuple which we cannot modify so instead  of the below line 
            #merged_list[-1][1] = max(merged_list[-1][1] , i[1])
            merged_list[-1] = (merged_list[-1][0], max(merged_list[-1][1], i[1]))
                    

    return merged_list



    """Return sorted merged intervals; touching endpoints count as overlap."""
    # TODO: Implement using a sorted copy and a scan.
    raise NotImplementedError("Implement merge_intervals before running checks")


def run_tests() -> None:
    cases = [
        ([], []),
        ([(2, 4)], [(2, 4)]),
        ([(8, 10), (1, 3), (2, 6), (15, 18)], [(1, 6), (8, 10), (15, 18)]),
        ([(1, 3), (3, 5)], [(1, 5)]),
        ([(1, 2), (3, 4)], [(1, 2), (3, 4)]),
        ([(1, 10), (2, 3), (4, 5)], [(1, 10)]),
        ([(1, 4), (1, 4)], [(1, 4)]),
        ([(1, 2), (1, 5)], [(1, 5)]),
        ([(5, 7), (1, 3), (3, 5)], [(1, 7)]),
        ([(-5, -2), (-3, 0), (2, 2)], [(-5, 0), (2, 2)]),
        ([(2, 2), (2, 3)], [(2, 3)]),
    ]
    for intervals, expected in cases:
        original = intervals.copy()
        result = merge_intervals(intervals)
        assert result == expected, f"For {original}: expected {expected}, got {result}"
        assert intervals == original, "Do not modify the input list"

    print("All Merge Intervals checks passed")


if __name__ == "__main__":
    run_tests()
