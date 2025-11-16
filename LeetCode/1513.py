# https://leetcode.com/problems/number-of-substrings-with-only-1s/

def numSub(s: str) -> int:
    r = 0

    for i in s.split("0"):
        c = i.count("1")
        
        r += (c + 1) * c // 2
        
    return r