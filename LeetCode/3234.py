# https://leetcode.com/problems/count-the-number-of-substrings-with-dominant-ones/

from collections import defaultdict

def numberOfSubstrings(s: str) -> int:
    n = len(s)

    z = [0] * (n + 1)
    zi = defaultdict(list)
    zi[0].append(0)

    for k in range(n):
        c = z[k] + (1 if s[k] == '0' else 0)
        z[k + 1] = c
        zi[c].append(k + 1)

    zmax = int(n ** 0.5)
    r = 0

    for i in range(n):
        base = z[i]
        
        for j in range(zmax + 1):
            c = base + j
            
            if c > z[n]: break

            l = j * j + j
            ei = i + l - 1

            if ei >= n: break
                
            mri = ei + 1

            if c in zi:
                k = zi[c]

                kmin = max(i + 1, mri)
                
                s = 0
                l, h = 0, len(k)
                
                while l < h:
                    m = (l + h) // 2
                    
                    if k[m] < kmin: l = m + 1
                    else: h = m
                    
                s = l

                r += (len(k) - s)

    return r