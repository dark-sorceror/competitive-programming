# https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k/

def hasAllCodes(s: str, k: int) -> bool:
    t = 1 << k
    n = len(s)

    c = set()

    for i in range(n - k + 1):
        sub = s[i : i + k]
        c.add(sub)
        
    return len(c) == t # (258 ms)