# https://leetcode.com/problems/count-unguarded-cells-in-the-grid/

def countUnguarded(m: int, n: int, guards: list[list[int]], walls: list[list[int]]) -> int:
    c = 0
    
    grid = [[0] *n for i in range(m)]

    for x, y in guards: grid[x][y] = 1
    for x, y in walls: grid[x][y] = 2

    directions = [
        (0, -1), # North
        (-1, 0), # West
        (1, 0), # East
        (0, 1) # South
    ]

    for gx, gy in guards:
        for dx, dy in directions:
            x, y = gx + dx, gy + dy
            
            while 0 <= x < m and 0 <= y < n:
                if grid[x][y] == 1 or grid[x][y] == 2: 
                    break
                else:
                    grid[x][y] = 3
                    
                x, y = x + dx, y + dy
                
    for i in grid:
        c += i.count(0)

    return c # (434 ms)