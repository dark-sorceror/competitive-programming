# https://leetcode.com/problems/minimum-absolute-difference/

def minimumAbsDifference(arr: list[int]) -> list[list[int]]:
    arr.sort()

    m = float('inf')

    for i in range(1, len(arr)):
        c = arr[i] - arr[i - 1]

        if c < m: m = c

    r = []

    for i in range(1, len(arr)):
        if arr[i] - arr[i - 1] == m:
            r.append([arr[i - 1], arr[i]])

    return r # (51 ms)