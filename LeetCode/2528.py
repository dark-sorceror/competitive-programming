# https://leetcode.com/problems/maximize-the-minimum-powered-city/

def maxPower(stations: list[int], r: int, k: int) -> int:
    if r == 0:
        l, h = min(stations), max(stations) + k
        r = l
        
        while l <= h:
            m = (l + h) // 2
            req = sum(max(0, m - i) for i in stations)
            
            if req <= k:
                r = m
                l = m + 1
            else: h = m - 1
                
        return r

    n, t, s = len(stations), [0], 0

    for i in range(n):
        s += stations[i]
        t.append(s)
        
    p = [t[min(n, i + r + 1)] - t[max(0, i - r)] for i in range(n)]

    def check(mp: int) -> bool:
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
                e = min(n, i + 2 * r + 1)
                t[e] -= need
                    
        return True

    l, h, ans = 0, sum(stations) + k, 0

    while l <= h:
        m = (l + h) // 2
        
        if check(m):
            ans = m
            l = m + 1
        else: h = m - 1

    return ans # (1361 ms)