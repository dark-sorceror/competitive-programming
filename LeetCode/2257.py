# https://leetcode.com/problems/count-unguarded-cells-in-the-grid/

def countUnguarded(m: int, n: int, guards: list[list[int]], walls: list[list[int]]) -> int:
    grid = [[0] *n for i in range(m)]

    for x, y in guards:
        grid[x][y] = 2
                
    for x, y in walls:
        grid[x][y] = -2

    directions = [
        (0, -1), # North
        (-1, 0), # West
        (1, 0), # East
        (0, 1) # South
    ]

    for x, y in guards:
        for dx, dy in directions:
            px = x + dx
            py = y + dy
            
            while 0 <= px < m and 0 <= py < n:
                if grid[px][py] == 2 or grid[px][py] == -2:
                    break
                else:
                    grid[px][py] = 1
                    
                px += dx
                py += dy

    s = 0     
    for i in grid:
        for j in i:
            if j == 0:
                s += 1

    return s
    