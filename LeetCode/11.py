# https://leetcode.com/problems/container-with-most-water/

def maxArea(height: list[int]) -> int:
    n = len(height)

    l, r, v = 0 , n - 1, 0

    while r >= l:
        h = min(height[l], height[r])
        w = r - l

        if (h * w) > v: v = h * w
            
        if height[r] > height[l]: l += 1
        elif height[r] <= height[l]: r -= 1
    
    return v # (55 ms)