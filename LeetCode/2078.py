# https://leetcode.com/problems/two-furthest-houses-with-different-colors/

def maxDistance(colors: list[int]) -> int:
    n = len(colors)

    l, r = 0, n - 1
    
    while colors[l] == colors[n - 1]:
        l += 1
    
    while colors[r] == colors[0]:
        r -= 1
        
    return max(n - 1 - l, r) # (0 ms)