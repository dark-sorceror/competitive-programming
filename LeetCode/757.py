# https://leetcode.com/problems/set-intersection-size-at-least-two/

def intersectionSizeTwo(intervals: list[list[int]]) -> int:
    intervals.sort(key = lambda x: (x[1], -x[0]))

    r = []
    a = b = -1

    for i, j in intervals:
        if i > b:
            r.append(j - 1)
            r.append(j)
            a, b = j - 1, j

        elif i > a:
            r.append(j)
            a, b = b, j

    return len(r) # (9 ms)