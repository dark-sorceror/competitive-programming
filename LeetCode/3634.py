# https://leetcode.com/problems/minimum-removals-to-balance-array/

from bisect import bisect_right

def minRemoval(nums: list[int], k: int) -> int:
    nums.sort()
    c = 0

    for i, j in enumerate(nums):
        x = bisect_right(nums, k * j)
        c = max(c, x - i)

    return len(nums) - c # (182 ms)