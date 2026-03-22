# https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation/

def findRotation(mat: list[list[int]], target: list[list[int]]) -> bool:
    for i in range(4):
        if mat == target:
            return True

        mat = [list(j) for j in zip(*mat[::-1])]

    return False # (0 ms)