# https://leetcode.com/problems/minimum-distance-between-three-equal-elements-i/

from collections import defaultdict

def minimumDistance(nums: list[int]) -> int:
    m = defaultdict(list)
    
    for i, j in enumerate(nums):
        m[j].append(i)
    
    a = float('inf')

    for i in m.values():
        if len(i) >= 3:
            for h in range(len(i) - 2):
                a = min(a, 2 * (i[h + 2] - i[h]))
    
    return a if a != float('inf') else -1 # (0 ms)