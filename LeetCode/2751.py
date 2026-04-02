# https://leetcode.com/problems/robot-collisions/

def survivedRobotsHealths(positions: list[int], healths: list[int], directions: str) -> list[int]:
    n = len(positions)
    r = []

    for i in range(n):
        r.append([positions[i], healths[i], directions[i], i])
    
    r.sort()
    
    # Stack for R
    s = []
    
    for p, h, d, i in r:
        if d == 'R':
            s.append([p, h, d, i])
        else:
            while s and s[-1][2] == 'R' and s[-1][1] < h:
                # L destroys R
                s.pop()

                h -= 1
            
            if not s or s[-1][2] == 'L':
                # L survives; no R to collide with
                s.append([p, h, d, i])
            elif s[-1][1] == h:
                # Both destroyed
                s.pop()
            else:
                # R destroys L
                s[-1][1] -= 1
    
    a = sorted(s, key = lambda i: i[3])

    return [i[1] for i in a] # (183 ms)