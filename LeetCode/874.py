# https://leetcode.com/problems/walking-robot-simulation/

def robotSim(commands: list[int], obstacles: list[list[int]]) -> int:
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    
    x, y, di = 0, 0, 0
    
    s = set(map(tuple, obstacles))
    
    m = 0
    
    for i in commands:
        if i == -2:
            di = (di - 1) % 4
        elif i == -1:
            di = (di + 1) % 4
        else:
            for j in range(i):
                next_x, next_y = x + dx[di], y + dy[di]

                if (next_x, next_y) not in s:
                    x, y = next_x, next_y
                    m = max(m, x * x + y * y)
                else:
                    break
                    
    return m # (31 ms)