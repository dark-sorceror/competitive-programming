# https://leetcode.com/problems/count-partitions-with-even-sum-difference/

def countPartitions(nums: list[int]) -> int:
    n, t = len(nums), sum(nums)

    if t % 2 != 0: return 0
    else: return n - 1 # (0 ms)