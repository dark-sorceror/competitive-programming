# https://leetcode.com/problems/maximum-matrix-sum/

def maxMatrixSum(matrix: list[list[int]]) -> int:
    t, m, c = 0, float('inf'), 0
    
    for i in matrix:
        for j in i:
            t += abs(j)
            m = min(m, abs(j))

            if j < 0: c += 1
                
    if c % 2 == 0: return t
    else: return t - 2 * m # (79 ms)