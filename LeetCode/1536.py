# https://leetcode.com/problems/minimum-swaps-to-arrange-a-binary-grid/

def minSwaps(grid: list[list[int]]) -> int:
    n = len(grid)
    z, a = [], 0

    for i in grid:
        c = 0

        for j in range(n - 1, -1, -1):
            if i[j] == 0: c += 1
            else: break

        z.append(c)

    for i in range(n):
        f = False
        
        for j in range(i, n):
            if z[j] >= (n - 1 - i):
                a += (j - i)
                z.insert(i, z.pop(j))
                f = True

                break
        
        if not f: return -1
            
    return a # (1 ms)