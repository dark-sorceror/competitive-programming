# https://leetcode.com/problems/maximize-area-of-square-hole-in-grid/

def maximizeSquareHoleArea(
    n: int, 
    m: int, 
    hBars: list[int], 
    vBars: list[int]
) -> int:
    def get_max_gap(b):
        b.sort()
        m, c = 1, 1
        
        for i in range(1, len(b)):
            if b[i] == b[i - 1] + 1: c += 1
            else: c = 1
            
            m = max(m, c)
        
        return m + 1

    m_h, m_v = get_max_gap(hBars), get_max_gap(vBars)

    return min(m_h, m_v) ** 2 # (0 ms)