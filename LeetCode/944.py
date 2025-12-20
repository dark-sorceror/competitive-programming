# https://leetcode.com/problems/delete-columns-to-make-sorted/

def minDeletionSize(strs: list[str]) -> int:
    r, c, j = 0, [], 0

    while j < len(strs[0]):
        for i in range(len(strs)):
            c.append(strs[i][j])
            
        if c != sorted(c): r += 1

        j += 1
        c.clear()

    return r # (59 ms)