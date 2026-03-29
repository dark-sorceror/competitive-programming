# https://leetcode.com/problems/check-if-strings-can-be-made-equal-with-operations-i/

def canBeEqual(s1: str, s2: str) -> bool:
    if s1[0] == s2[2] and s1[1] == s2[3]:
        return True
        
    return False