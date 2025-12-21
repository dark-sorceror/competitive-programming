# https://leetcode.com/problems/delete-columns-to-make-sorted-ii/

def minDeletionSize(strs: list[str]) -> int:
    r, c, j = 0, ["" for i in strs], 0

    if strs == sorted(strs): return 0

    while j < len(strs[0]):
        t = c[:]

        for i in range(len(strs)):
            t[i] += strs[i][j]
            
        if t != sorted(t):  r += 1
        else: c = t[:]

        j += 1

    return r # (15 ms)