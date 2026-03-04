# https://leetcode.com/problems/special-positions-in-a-binary-matrix/

def numSpecial(mat: list[list[int]]) -> int:
    m, n = len(mat), len(mat[0])
    rc = [0] * m
    cc = [0] * n
    a = 0
    
    for r in range(m):
        for c in range(n):
            if mat[r][c] == 1:
                rc[r] += 1
                cc[c] += 1

    for r in range(m):
        for c in range(n):
            if mat[r][c] == 1 and rc[r] == 1 and cc[c] == 1:
                a += 1

    return a # (1 ms)