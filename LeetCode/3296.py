# https://leetcode.com/problems/minimum-number-of-seconds-to-make-mountain-height-zero/

import math

def minNumberOfSeconds(mountainHeight: int, workerTimes: list[int]) -> int:
    def can_finish(t):
        total = 0

        for w in workerTimes:
            x = int((-1 + math.sqrt(1 + 8 * t / w)) / 2)
            total += x

            if total >= mountainHeight:
                return True

        return total >= mountainHeight

    l = 0
    f = min(workerTimes)
    h = f * mountainHeight * (mountainHeight + 1) // 2
    
    a = h

    # Binary Search
    while l <= h:
        m = (l + h) // 2

        if can_finish(m):
            a = m
            h = m - 1
        else:
            l = m + 1
    return a # (198 ms)