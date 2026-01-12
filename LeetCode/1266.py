# https://leetcode.com/problems/minimum-time-visiting-all-points/

def minTimeToVisitAllPoints(points: list[list[int]]) -> int:
    t = 0

    for i, j in zip(points, points[1:]):
        t += max(abs(i[0] - j[0]), abs(i[1] - j[1]))

    return t # (0 ms)