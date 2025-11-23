# https://leetcode.com/problems/unique-length-3-palindromic-subsequences/

from string import ascii_lowercase

def countPalindromicSubsequence(s: str) -> int:
    r = 0

    for i in ascii_lowercase:
        f, l = s.find(i), s.rfind(i)

        if f != -1 and f < l:
            m = s[f + 1: l]
            
            r += len(set(m))
            
    return r # (147 ms)