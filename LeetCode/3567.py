# https://leetcode.com/problems/minimum-absolute-difference-in-sliding-submatrix/

def minAbsDiff(grid: list[list[int]], k: int) -> list[list[int]]:
    m, n = len(grid), len(grid[0])
    a = [[0] * (n - k + 1) for _ in range(m - k + 1)]
    
    for i in range(m - k + 1):
        for j in range(n - k + 1):
            s = []

            for r in range(i, i + k):
                for c in range(j, j + k):
                    s.append(grid[r][c])
            
            s.sort()
            
            m_diff = float('inf')

            for t in range(1, len(s)):
                if s[t] != s[t - 1]:
                    m_diff = min(m_diff, s[t] - s[t - 1])
            
            a[i][j] = m_diff if m_diff != float('inf') else 0
            
    return a