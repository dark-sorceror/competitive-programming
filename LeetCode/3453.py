# https://leetcode.com/problems/separate-squares-i/

def separateSquares(squares: list[list[int]]) -> float:
    t = sum(l * l for x, y, l in squares)
    
    def get_area(t_y: float) -> float:
        a = 0.0
        
        for x, y, l in squares:
            if t_y <= y: continue
            elif t_y >= y + l: a += l * l
            else: a += l * (t_y - y)

        return a

    l = min(y for x, y, l in squares)
    h = max(y + l for x, y, l in squares)

    # Binary Search
    for i in range(100):
        m = (l + h) / 2

        if get_area(m) < (t / 2): l = m
        else: h = m
            
    return l # (4022 ms)