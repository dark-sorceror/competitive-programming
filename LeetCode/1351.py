# https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/

def countNegatives(grid: list[list[int]]) -> int:
    # O (m log n)
    t = 0
    
    for i in range(len(grid)):
        left, right, z = 0, len(grid[i]) - 1, -1
        
        while left <= right:
            mid = (left + right) // 2

            if grid[i][mid] < 0:
                z = mid
                right = mid - 1
            else: left = mid + 1
        
        if z != -1: t += len(grid[i]) - z
    
    return t # (0 ms)
    
    # O (m * n)
    """
    t = 0

    for i in grid:
        for j in i:
            if j < 0:
                t += 1
    
    return t
    """

grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]

print(countNegatives(grid))