# Incomplete
# https://leetcode.com/problems/minimum-operations-to-convert-all-elements-to-zero/

def minOperations(nums: list[int]) -> int:
    i, r = 0, 0
    
    def dfs(l, r):
        i, res, m = l, 1, min(nums[l:r])

        while i <= (r - 1):
            if nums[i] == m:
                i += 1
                
                continue
            
            j = i
            
            while j <= (r - 1) and nums[j] != m:
                j += 1
                
            res += dfs(i, j)
            i = j
        
        return res

    while i < len(nums):
        if nums[i] == 0:
            i += 1
            
            continue
        
        j = i
        
        while j < len(nums) and nums[j] != 0:
            j += 1
 
        r += dfs(i, j)
        i = j
        
    return r