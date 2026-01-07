# https://leetcode.com/problems/is-subsequence/

def isSubsequence(s: str, t: str) -> bool:
    if not s: return True

    l = r = 0

    while r < len(t):
        if l >= len(s): return True
            
        if s[l] == t[r]:
            l += 1
            r += 1
        else: r += 1
    
    return l == len(s) # (0 ms)