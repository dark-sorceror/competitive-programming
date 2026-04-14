# https://leetcode.com/problems/minimum-distance-to-the-target-element/

def getMinDistance(nums: list[int], target: int, start: int) -> int:
    m = float('inf')

    for i, j in enumerate(nums):
        if j == target:
            m = min(m, abs(i - start))

    return m # (0 ms)