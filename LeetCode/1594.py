# https://leetcode.com/problems/maximum-non-negative-product-in-a-matrix/

def maxProductPath(grid: list[list[int]]) -> int:
    m, n = len(grid), len(grid[0])
    dp_max = [[0] * n for _ in range(m)]
    dp_min = [[0] * n for _ in range(m)]
    
    dp_max[0][0] = dp_min[0][0] = grid[0][0]
    
    for j in range(1, n):
        dp_max[0][j] = dp_min[0][j] = dp_max[0][j - 1] * grid[0][j]

    for i in range(1, m):
        dp_max[i][0] = dp_min[i][0] = dp_max[i - 1][0] * grid[i][0]
        
    for i in range(1, m):
        for j in range(1, n):
            if grid[i][j] >= 0:
                dp_max[i][j] = max(dp_max[i - 1][j], dp_max[i][j - 1]) * grid[i][j]
                dp_min[i][j] = min(dp_min[i - 1][j], dp_min[i][j - 1]) * grid[i][j]
            else:
                dp_max[i][j] = min(dp_min[i - 1][j], dp_min[i][j - 1]) * grid[i][j]
                dp_min[i][j] = max(dp_max[i - 1][j], dp_max[i][j - 1]) * grid[i][j]

    return dp_max[m - 1][n - 1] % (10 ** 9 + 7) if dp_max[m - 1][n - 1] >= 0 else -1 # (0 ms)