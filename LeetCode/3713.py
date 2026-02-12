# https://leetcode.com/problems/longest-balanced-substring-i/

def longestBalanced(s: str) -> int:
    n = len(s)
    m = 0
    
    for i in range(n):
        cc = {}

        for j in range(i, n):
            c = s[j]
            cc[c] = cc.get(c, 0) + 1
            
            f = list(cc.values())

            if len(set(f)) == 1:
                m = max(m, j - i + 1)
                
    return m # (3045 ms)