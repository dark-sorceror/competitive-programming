# https://leetcode.com/problems/maximum-average-subarray-i/

def findMaxAverage(nums: list[int], k: int) -> float:
    r = s = sum(nums[:k])

    for i in range(k, len(nums)):
        s += nums[i] - nums[i - k]
        r = max(r, s)

    return r / k # (52 ms)