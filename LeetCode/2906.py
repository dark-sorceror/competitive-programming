# https://leetcode.com/problems/construct-product-matrix/

def constructProductMatrix(grid: list[list[int]]) -> list[list[int]]:
    n, m = len(grid), len(grid[0])
    p = [[0] * m for _ in range(n)]
    
    c = 1

    for i in range(n):
        for j in range(m):
            p[i][j] = c
            c = (c * grid[i][j]) % 12345
            
    c = 1

    for i in range(n - 1, -1, -1):
        for j in range(m - 1, -1, -1):
            p[i][j] = (p[i][j] * c) % 12345
            c = (c * grid[i][j]) % 12345
            
    return p # (95 ms)