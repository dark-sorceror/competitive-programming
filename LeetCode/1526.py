# https://leetcode.com/problems/minimum-number-of-increments-on-subarrays-to-form-a-target-array/

def minNumberOperations(target: list[int]) -> int:
    o = 0
    p = 0

    for i in target:
        d = i - p

        if d > 0:
            o += d

        p = i
    
    return o # (28 ms)