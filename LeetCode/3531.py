# https://leetcode.com/problems/count-covered-buildings/

def countCoveredBuildings(n: int, buildings: list[list[int]]) -> int:
    c = 0

    minxr, maxxr = [n + 1] * (n + 1), [0] * (n + 1)
    minyc, maxyc = [n + 1] * (n + 1), [0] * (n + 1)

    for x, y in buildings:
        minxr[y], maxxr[y] = min(minxr[y], x), max(maxxr[y], x)
        minyc[x], maxyc[x] = min(minyc[x], y), max(maxyc[x], y)
    
    for x, y in buildings:  
        rb, cb = (x == minxr[y]) or (x == maxxr[y]), (y == minyc[x]) or (y == maxyc[x])
        
        if not rb and not cb: c += 1
            
    return c # (442 ms)