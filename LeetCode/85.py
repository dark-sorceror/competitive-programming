# https://leetcode.com/problems/maximal-rectangle/

def maximalRectangle(matrix: list[list[str]]) -> int:
    r, c = len(matrix), len(matrix[0])
    h = [0] * (c + 1)
    a = 0
    
    for i in matrix:
        for j in range(c):
            if i[j] == "1": h[j] = h[j] + 1
            else: h[j] = 0

        s = [-1]

        # Monotonic Stack
        for j in range(len(h)):
            while h[j] < h[s[-1]]:
                c_h = h[s.pop()]
                w = j - s[-1] - 1
                a = max(a, c_h * w)

            s.append(j)
            
    return a # (17 ms)

matrix =[["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
print(maximalRectangle(matrix))