# https://leetcode.com/problems/count-number-of-trapezoids-i/

from collections import defaultdict

def countTrapezoids(points: list[list[int]]) -> int:
    y_groups = defaultdict(list)

    for x, y in points:
        y_groups[y].append(x)

    y_coords = [y for y in y_groups if len(y_groups[y]) > 1]
    
    if len(y_coords) < 2: return 0
        
    t = 0

    for i in range(len(y_coords)):
        ya = y_coords[i]
        na = len(y_groups[ya])

        ca = (na * (na - 1)) // 2
        
        for j in range(i + 1, len(y_coords)):
            yd = y_coords[j]
            nd = len(y_groups[yd])

            cd = (nd * (nd - 1)) // 2
            p = (ca * cd)
            t = (t + p) % 10**9 + 7

    return t