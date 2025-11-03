# https://leetcode.com/problems/count-unguarded-cells-in-the-grid/

def countUnguarded(m: int, n: int, guards: list[list[int]], walls: list[list[int]]) -> int:
    grid = []
    
    for i in range(m):
        grid.append([j*0 for j in range(n)])
        
    for i in guards:
        for j in range(n):
            if [i[0], j] == i:
                grid[i[0]][j] = 2
            #else:
            #    grid[i[0]][j] = 1
        for j in range(m):
            if [j, i[1]] == i:
                grid[j][i[1]] = 2
            #else:
            #    grid[j][i[1]] = 1
                
    for i in walls:
        for j in range(n):
            if [i[0], j] == i:
                grid[i[0]][j] = -2
        for j in range(m):
            if [j, i[1]] == i:
                grid[j][i[1]] = -2

    transpose = []

    for i in range(n):
        transpose.append([])

    for r in grid:
        if r.count(2) == r.count(-2) and r.count(2) > 0:
            if r.index(2) < r.index(-2):
                guarded = True
            else:
                guarded = False
        else:
            if r.count(-2) == r.count(2) == 0:
                guarded = False
            elif r.count(-2) == 0:
                guarded = True
            else:
                guarded = False
                
        for i in range(n):
            if r[i] == 2:
                guarded = True
                
            elif r[i] == -2:
                guarded = False
            
            else:
                if not guarded:
                    grid[grid.index(r)][i] = 0
                else:
                    grid[grid.index(r)][i] = 1
                    
            transpose[i].append(r[i])

    for r in transpose:
        if r.count(2) == r.count(-2) and r.count(2) > 0:
            if r.index(2) < r.index(-2):
                guarded = True
            else:
                guarded = False
        else:
            if r.count(-2) == r.count(2) == 0:
                guarded = False
            elif r.count(-2) == 0:
                guarded = True
            else:
                guarded = False
                
        for i in range(m):
            if r[i] == 2:
                guarded = True
                
            elif r[i] == -2:
                guarded = False
            
            else:
                if guarded:
                    transpose[transpose.index(r)][i] = 1

    s = 0
    
    for i in transpose:
        s += sum(i)
        
    print(m * n - len(guards) - len(walls) - s)