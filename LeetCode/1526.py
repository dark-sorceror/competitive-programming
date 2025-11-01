# https://leetcode.com/problems/minimum-number-of-increments-on-subarrays-to-form-a-target-array/

def minNumberOperations(target: list[int]) -> int:
    operations = 0
    prev = 0

    for i in target:
        d = i - prev

        if d > 0:
            operations += d

        prev = i
    
    return operations # (28 ms)