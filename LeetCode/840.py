# https://leetcode.com/problems/magic-squares-in-grid/

def numMagicSquaresInside(grid: list[list[int]]) -> int:
    r, c = len(grid), len(grid[0])
    count = 0

    def is_magic(r, c):
        vs = set()

        for i in range(r, r + 3):
            for j in range(c, c + 3):
                v = grid[i][j]

                if v < 1 or v > 9: return False
                vs.add(v)

        if len(vs) != 9: return False

        if (grid[r][c] + grid[r][c + 1] + grid[r][c + 2] != 15 or
            grid[r + 1][c] + grid[r + 1][c + 1] + grid[r + 1][c + 2] != 15 or
            grid[r + 2][c] + grid[r + 2][c + 1] + grid[r + 2][c + 2] != 15):
            return False

        if (grid[r][c] + grid[r + 1][c] + grid[r + 2][c] != 15 or
            grid[r][c + 1] + grid[r + 1][c + 1] + grid[r + 2][c + 1] != 15 or
            grid[r][c + 2] + grid[r + 1][c + 2] + grid[r + 2][c + 2] != 15):
            return False

        if (grid[r][c] + grid[r + 1][c + 1] + grid[r + 2][c + 2] != 15 or
            grid[r][c + 2] + grid[r + 1][c + 1] + grid[r + 2][c] != 15):
            return False
            
        return True

    for i in range(r - 2):
        for j in range(c - 2):
            if grid[i+1][j+1] != 5: continue
            if is_magic(i, j): count += 1
                
    return count # (0 ms)