# https://leetcode.com/problems/equal-sum-grid-partition-i/

def canPartitionGrid(grid: list[list[int]]) -> bool:
    m, n = len(grid), len(grid[0])
    s = sum(sum(i) for i in grid)
    
    t = s // 2
    
    r = 0

    for i in range(m - 1):
        r += sum(grid[i])

        if r == t:
            return True
            
    c = 0

    for j in range(n - 1):
        for i in range(m):
            c += grid[i][j]

        if c == t:
            return True
            
    return False