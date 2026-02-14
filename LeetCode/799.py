# https://leetcode.com/problems/champagne-tower/

def champagneTower(poured: int, query_row: int, query_glass: int) -> float:
    t = [[0 for i in range(102)] for i in range(102)]

    t[0][0] = float(poured)
    
    for r in range(query_row + 1):
        for c in range(r + 1):
            e = (t[r][c] - 1.0) / 2.0

            if e > 0:
                t[r + 1][c] += e
                t[r + 1][c + 1] += e
                t[r][c] = 1.0
                
    return min(1.0, t[query_row][query_glass]) # (123 ms)