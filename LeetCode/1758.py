# https://leetcode.com/problems/minimum-changes-to-make-alternating-binary-string/

def minOperations(s: str) -> int:
    a = 0
    
    for i, j in enumerate(s):
        if i % 2 == 0:
            if j != '0':
                a += 1
        else:
            if j != '1':
                a += 1

    return min(a, len(s) - a) # (1 ms)