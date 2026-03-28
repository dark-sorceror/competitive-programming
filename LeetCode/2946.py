# https://leetcode.com/problems/matrix-similarity-after-cyclic-shifts/

def areSimilar(mat: list[list[int]], k: int) -> bool:
    m = len(mat)
    n = len(mat[0])
    e = k % n

    for i in range(m):
        for j in range(n):
            if i % 2 == 0:
                if mat[i][j] != mat[i][(j + e) % n]:
                    return False
            else:
                if mat[i][j] != mat[i][(j - e + n) % n]:
                    return False

    return True