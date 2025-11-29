# https://leetcode.com/problems/minimum-operations-to-make-array-sum-divisible-by-k/

def minOperations(nums: list[int], k: int) -> int:
    c = sum(nums)
    r = c % k

    return r # (0 ms)