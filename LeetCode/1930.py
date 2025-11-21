from string import ascii_lowercase

def countPalindromicSubsequence(s: str) -> int:
    r = 0

    for i in ascii_lowercase:
        f = s.find(i)
        l = s.rfind(i)

        if f != -1 and f < l:
            m = s[f + 1: l]
            
            r += len(set(m))
            
    return r