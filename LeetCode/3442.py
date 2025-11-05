# https://leetcode.com/problems/maximum-difference-between-even-and-odd-frequency-i/

def maxDifference(s: str) -> int:
    c = dict()
    
    for i in s:
        c[i] = c.get(i, 0) + 1
        
    mof, mef = -1, float('inf')

    for i in c.values():
        if i % 2 != 0: mof = max(mof, i)
        else: mef = min(mef, i)
    
    if mof != mef and mof != -1: return mof - mef
    else: return 0 # (0 ms)