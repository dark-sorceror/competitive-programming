# https://leetcode.com/problems/minimum-difference-between-highest-and-lowest-of-k-scores/

def minimumDifference(nums: list[int], k: int) -> int:
    nums.sort()

    m = float('inf')
    
    for i in range(len(nums) - k + 1):
        c = nums[i + k - 1] - nums[i]
        m = min(m, c)
        
    return m # (3 ms)