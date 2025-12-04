# https://leetcode.com/problems/count-number-of-trapezoids-ii/

def gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b

    return a

def get_slope(p1: int, p2: int) -> int:
    x1, y1 = p1
    x2, y2 = p2
    dy = y2 - y1
    dx = x2 - x1
    
    if dx == 0: return (1, 0)

    cd = gcd(abs(dy), abs(dx))
    
    sdy = dy // cd
    sdx = dx // cd

    if sdx < 0:
        sdx = -sdx
        sdy = -sdy
    
    return (sdy, sdx)

def countTrapezoids(points: list[list[int]]) -> int:
    n = len(points)

    if n < 4: return 0

    s = set()

    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                for l in range(k + 1, n):
                    P = [points[i], points[j], points[k], points[l]]
                    I = tuple(sorted((i, j, k, l)))

                    s_01 = get_slope(P[0], P[1])
                    s_02 = get_slope(P[0], P[2])
                    s_03 = get_slope(P[0], P[3])
                    s_12 = get_slope(P[1], P[2])
                    s_13 = get_slope(P[1], P[3])
                    s_23 = get_slope(P[2], P[3])

                    t = False

                    if s_01 == s_23 or s_12 == s_03: t = True
                    elif s_02 == s_13 or s_12 == s_03: t = True
                    elif s_01 == s_23 or s_13 == s_02: t = True
                    if t: s.add(I)
                        
    return len(s)