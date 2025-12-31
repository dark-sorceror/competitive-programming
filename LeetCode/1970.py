# https://leetcode.com/problems/last-day-where-you-can-still-cross/

def latestDayToCross(row: int, col: int, cells: list[list[int]]) -> int:
    left, right, o = 1, len(cells), 0
            
    def can_cross(day: int):
        g = [[0] * col for _ in range(row)]

        for i in range(day):
            r, c = cells[i]
            g[r - 1][c - 1] = 1

        s = []

        for i in range(col):
            if g[0][i] == 0:
                s.append((0, i))
                g[0][i] = -1

        # DFS
        while s:
            r, c = s.pop()

            if r == row - 1: return True

            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < row and 0 <= nc < col and g[nr][nc] == 0:
                    g[nr][nc] = -1
                    s.append((nr, nc))
        
        return False

    # Binary Search
    while left <= right:
        m = (left + right) // 2

        if can_cross(m):
            o = m
            left = m + 1
        else: right = m - 1
            
    return o # (692 ms)