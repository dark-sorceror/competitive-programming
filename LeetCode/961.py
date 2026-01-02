# https://leetcode.com/problems/n-repeated-element-in-size-2n-array/

def repeatedNTimes(nums: list[int]) -> int:
    # O (1)
    for i in range(len(nums) - 2):
        if nums[i] == nums[i + 1] or nums[i] == nums[i + 2]: return nums[i]
        
    return nums[-1] # (0 ms)
        
    """ O (n x n)
    nums = sorted(nums)

    for i in range(len(nums)):
        if nums[i + 1] == nums[i]:
            return nums[i]
    """