# https://leetcode.com/problems/two-sum/

def twoSum(nums: list[int], target: int) -> list[int]:
    # Solution 1 ( O(n^2) ) ~ looping through each element twice; not the best solution
    """
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i] + nums[j] == target: return [i, j]
    """
            
    # Solution 2 ( O(n) ) ~ hash map; the most optimal time complexity
    m = dict()
    
    for i, j in enumerate(nums):
        d = target - j
        
        if d in m: return [m[d], i]
        
        m[j] = i # (0 ms)