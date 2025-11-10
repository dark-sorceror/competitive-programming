# https://leetcode.com/problems/minimum-operations-to-convert-all-elements-to-zero/

def minOperations(nums: list[int]) -> int:
    if all(i == 0 for i in nums): return 0
    
    m = min(i for i in nums if i > 0)

    nums = [0 if i == m else i for i in nums]

    s, t = [], []

    for i in nums:
        if i == 0:
            if t:
                s.append(t)
                t = []
        else: t.append(i)
    if t: s.append(t)

    return 1 + sum(minOperations(i) for i in s)