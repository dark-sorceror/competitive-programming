# https://leetcode.com/problems/flip-square-submatrix-vertically/

def reverseSubmatrix(grid: list[list[int]], x: int, y: int, k: int) -> list[list[int]]:
    for i in range(x, x + k // 2):
        n = x + k - 1 - (i - x)

        for j in range(y, y + k):
            grid[i][j], grid[n][j] = grid[n][j], grid[i][j]
    
    return grid # (0 ms)