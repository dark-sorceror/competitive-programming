# https://leetcode.com/problems/maximum-side-length-of-a-square-with-sum-less-than-or-equal-to-threshold/

def maxSideLength(mat: list[list[int]], threshold: int) -> int:
    m, n = len(mat), len(mat[0])

    p = [[0] * (n + 1) for i in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            p[i][j] = p[i - 1][j] + p[i][j - 1] - p[i - 1][j - 1] + mat[i - 1][j - 1]

    def is_valid(k: int):
        for i in range(k, m + 1):
            for j in range(k, n + 1):
                c = p[i][j] - p[i - k][j] - p[i][j - k] + p[i - k][j - k]
                
                if c <= threshold: return True

        return False

    l, h, a = 0, min(m, n), 0

    # Binary Search
    while l <= h:
        mid = (l + h) // 2

        if is_valid(mid):
            a = mid
            l = mid + 1
        else: h = mid - 1
            
    return a # (223 ms)