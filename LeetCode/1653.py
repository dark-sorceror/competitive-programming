# https://leetcode.com/problems/minimum-deletions-to-make-string-balanced/

def minimumDeletions(s: str) -> int:
    n = len(s)
    f = [0] * (n + 1)
    p = 0

    for i, j in enumerate(s):
        if j == 'b':
            f[i + 1] = f[i]
            p += 1
        else:
            f[i + 1] = min(f[i] + 1, p)

    return f[n] # (279 ms)