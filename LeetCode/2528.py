# https://leetcode.com/problems/maximize-the-minimum-powered-city/

def maxPower(stations: list[int], r: int, k: int) -> int:
    if r == 0: return min(stations)
    
    n, t, s = len(stations), [0], 0

    for i in range(n):
        s += stations[i]
        t.append(s)
        
    p = [t[min(n, i + r + 1)] - t[max(0, i - r)] for i in range(n)]

    def check(mp):
        t = [0] * (n + 1)
        a = 0
        rem = k
        
        for i in range(n):
            a += t[i]
            c = p[i] + a
            
            if c < mp:
                need = mp - c
                
                if (need) > rem: return False
                
                rem -= need
                a += need
                e = min(i + r, n -1) + r + 1
                
                if e < n: t[e] -= need
                    
        return True

    l, h, r = 0, sum(stations) + k, 0

    while l <= h:
        m = (l + h) // 2
        
        if check(m):
            r = m
            l = m + 1
        else: h = m - 1

    return r