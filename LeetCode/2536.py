# https://leetcode.com/problems/increment-submatrices-by-one/

def rangeAddQueries(n, queries):
    d = [[0] * (n + 1) for i in range(n + 1)]

    for r1, c1, r2, c2 in queries:
        d[r1][c1] += 1
        d[r1][c2 + 1] -= 1
        d[r2 + 1][c1] -= 1
        d[r2 + 1][c2 + 1] += 1
    
    for r in range(n):
        curr = 0

        for c in range(n):
            curr += d[r][c]
            d[r][c] = curr
    
    for c in range(n):
        curr = 0

        for r in range(n):
            curr += d[r][c]
            d[r][c] = curr
    
    return [r[:n] for r in d[:n]] # (235 ms)