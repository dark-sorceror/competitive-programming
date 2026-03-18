# https://leetcode.com/problems/count-submatrices-with-top-left-element-and-sum-less-than-k/

def countSubmatrices(grid: list[list[int]], k: int) -> int:
    m, n = len(grid), len(grid[0])
    p = [[0] * n for _ in range(m)]
    c = 0

    for i in range(m):
        for j in range(n):
            v = grid[i][j]
            t = p[i - 1][j] if i > 0 else 0
            l = p[i][j - 1] if j > 0 else 0
            o = p[i - 1][j - 1] if i > 0 and j > 0 else 0
            
            c_sum = v + t + l - o
            p[i][j] = c_sum
            
            if c_sum <= k:
                c += 1
            else:
                pass

    return c # (327 ms)