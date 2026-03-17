# https://leetcode.com/problems/get-biggest-three-rhombus-sums-in-a-grid/

def getBiggestThree(grid: list[list[int]]) -> list[int]:
    m, n = len(grid), len(grid[0])
    sums = set()

    for r in range(m):
        for c in range(n):
            sums.add(grid[r][c])
            
            for k in range(1, min(m, n)):
                if r - k < 0 or r + k >= m or c - k < 0 or c + k >= n:
                    break
                
                c_sum = 0
                
                for i in range(k):
                    c_sum += grid[r - k + i][c + i]
                    c_sum += grid[r + i][c + k - i]
                    c_sum += grid[r + k - i][c - i]
                    c_sum += grid[r - i][c - k + i]

                sums.add(c_sum)

    return sorted(list(sums), reverse = True)[:3] # (656 ms)