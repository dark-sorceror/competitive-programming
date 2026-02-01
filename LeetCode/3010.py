# https://leetcode.com/problems/divide-an-array-into-subarrays-with-minimum-cost-i/

def minimumCost(nums: list[int]) -> int:
    f = nums[0]
    r = sorted(nums[1:])
    
    return f + r[0] + r[1] # (0 ms)