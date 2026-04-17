# https://leetcode.com/problems/closest-equal-element-queries/

def solveQueries(nums: list[int], queries: list[int]) -> list[int]:
    n = len(nums)
    m = 2 * n
    d = [m] * m
    
    l = {}
    for i in range(m):
        x = nums[i % n]

        if x in l:
            d[i] = min(d[i], i - l[x])

        l[x] = i
        
    r = {}
    for i in range(m - 1, -1, -1):
        x = nums[i % n]

        if x in r:
            d[i] = min(d[i], r[x] - i)

        r[x] = i
        
    a = []
    for i in queries:
        x = min(d[i], d[i + n])
        a.append(x if x < n else -1)
        
    return a # (462 ms)