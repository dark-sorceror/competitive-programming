# https://leetcode.com/problems/minimum-cost-path-with-teleportations/

from collections import defaultdict

def minCost(grid: list[list[int]], k: int) -> int:
    m, n = len(grid), len(grid[0])
    f = [[[int('inf')] * n for _ in range(m)] for _ in range(k + 1)]
    f[0][0][0] = 0

    for i in range(m):
        for j in range(n):
            if i:
                f[0][i][j] = min(f[0][i][j], f[0][i - 1][j] + grid[i][j])
            if j:
                f[0][i][j] = min(f[0][i][j], f[0][i][j - 1] + grid[i][j])

    g = defaultdict(list)

    for i, row in enumerate(grid):
        for j, x in enumerate(row):
            g[x].append((i, j))

    keys = sorted(g, reverse = True)

    for t in range(1, k + 1):
        mn = int('inf')

        for key in keys:
            pos = g[key]

            for i, j in pos:
                mn = min(mn, f[t - 1][i][j])

            for i, j in pos:
                f[t][i][j] = mn

        for i in range(m):
            for j in range(n):
                if i:
                    f[t][i][j] = min(f[t][i][j], f[t][i - 1][j] + grid[i][j])
                if j:
                    f[t][i][j] = min(f[t][i][j], f[t][i][j - 1] + grid[i][j])
                    
    return min(f[t][m - 1][n - 1] for t in range(k + 1)) # (3651 ms)