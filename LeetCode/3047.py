# https://leetcode.com/problems/find-the-largest-area-of-square-inside-two-rectangles/

def largestSquareArea(bottomLeft: list[list[int]], topRight: list[list[int]]) -> int:
    n = len(bottomLeft)
    m = 0
    
    for i in range(n):
        for j in range(i + 1, n):
            a_x1, a_y1 = bottomLeft[i]
            a_x2, a_y2 = topRight[i]
            b_x1, b_y1 = bottomLeft[j]
            b_x2, b_y2 = topRight[j]
            
            i_x1, i_y1 = max(a_x1, b_x1), max(a_y1, b_y1)
            i_x2, i_y2 = min(a_x2, b_x2), min(a_y2, b_y2)
            
            w, h = i_x2 - i_x1, i_y2 - i_y1
            
            if w > 0 and h > 0:
                s = min(w, h)

                if s > m: m = s
                    
    return m ** 2 # (2537 ms)