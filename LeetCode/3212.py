# https://leetcode.com/problems/count-submatrices-with-equal-frequency-of-x-and-y/

def numberOfSubmatrices(grid: list[list[str]]) -> int:
    R, C = len(grid), len(grid[0])

    prefX = [[0] * (C + 1) for _ in range(R + 1)]
    prefY = [[0] * (C + 1) for _ in range(R + 1)]
    
    a = 0
    for r in range(R):
        for c in range(C):
            prefX[r + 1][c + 1] = prefX[r][c + 1] + prefX[r + 1][c] - prefX[r][c] + (1 if grid[r][c] == 'X' else 0)
            prefY[r + 1][c + 1] = prefY[r][c + 1] + prefY[r + 1][c] - prefY[r][c] + (1 if grid[r][c] == 'Y' else 0)
            
            if prefX[r + 1][c + 1] > 0 and prefX[r + 1][c + 1] == prefY[r + 1][c + 1]:
                a += 1
                
    return a # (1075 ms)