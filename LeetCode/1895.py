# https://leetcode.com/problems/largest-magic-square/

def largestMagicSquare(grid: list[list[int]]) -> int:
    m, n = len(grid), len(grid[0])
    
    s_r = [[0] * (n + 1) for i in range(m)]
    s_c = [[0] * n for i in range(m + 1)]
    
    for i in range(m):
        for j in range(n):
            s_r[i][j + 1] = s_r[i][j] + grid[i][j]
            s_c[i + 1][j] = s_c[i][j] + grid[i][j]
    
    for k in range(min(m, n), 1, -1):
        for i in range(m - k + 1):
            for j in range(n - k + 1):
                t = s_r[i][j + k] - s_r[i][j]
                
                match = True

                for r in range(i + 1, i + k):
                    r_s = s_r[r][j + k] - s_r[r][j]

                    if r_s != t:
                        match = False

                        break

                if not match: continue
                
                for c in range(j, j + k):
                    c_s = s_c[i + k][c] - s_c[i][c]

                    if c_s != t:
                        match = False

                        break

                if not match: continue
                
                d1, d2 = 0, 0

                for d in range(k):
                    d1 += grid[i + d][j + d]
                    d2 += grid[i + d][j + k - 1 - d]
                
                if d1 == t and d2 == t: return k
                    
    return 1 # (59 ms)