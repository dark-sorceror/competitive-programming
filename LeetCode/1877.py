# https://leetcode.com/problems/minimize-maximum-pair-sum-in-array/description/?envType=daily-question&envId=2026-01-24

def minPairSum(nums: list[int]) -> int:
    nums.sort()
    
    m, l, r = 0, 0, len(nums) - 1

    while l < r:
        c = nums[l] + nums[r]

        m = max(m, c)

        l += 1
        r -= 1
        
    return m # (835 ms)