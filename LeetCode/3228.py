# https://leetcode.com/problems/maximum-number-of-operations-to-move-ones-to-the-end/

def maxOperations(s: str) -> int:
    r, o = 0, 0

    for i, j in enumerate(s):
        if j == '1': o += 1
        elif i > 0 and s[i - 1] == '1': r += o

    return r # (87 ms)