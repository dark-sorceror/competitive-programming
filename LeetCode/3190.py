# https://leetcode.com/problems/find-minimum-operations-to-make-all-elements-divisible-by-three/

def minimumOperations(nums: list[int]) -> int:
    o = 0
    
    for num in nums:
        if num % 3 != 0: o += 1
            
    return o # (0 ms)