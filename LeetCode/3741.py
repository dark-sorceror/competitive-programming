# https://leetcode.com/problems/minimum-distance-between-three-equal-elements-ii/

from collections import defaultdict

def minimumDistance(nums: list[int]) -> int:
    m = defaultdict(list)
    a = float('inf')

    for i, j in enumerate(nums):
        m[j].append(i)
    
    for i in m.values():
        if len(i) < 3:
            continue
        
        for h in range(len(i) - 2):
            c = (i[h + 2] - i[h]) * 2
            a = min(a, c)
    
    return a if a != float('inf') else -1 # (322 ms)