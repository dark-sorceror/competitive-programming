# https://leetcode.com/problems/count-binary-substrings/?envType=daily-question&envId=2026-02-19

def countBinarySubstrings(s: str) -> int:
    g, c, a = [], 1, 0

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            c += 1
        else:
            g.append(c)
            c = 1

    g.append(c)
    
    for i in range(1, len(g)):
        a += min(g[i - 1], g[i])

    return a # (72 ms)