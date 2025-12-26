# https://leetcode.com/problems/minimum-penalty-for-a-shop/

def bestClosingTime(customers: str) -> int:
    c = customers.count('Y')
    
    m, h = c, 0
    h = 0

    for i, j in enumerate(customers):
        if j == 'Y': c -= 1
        else: c += 1
        
        if c < m:
            m = c
            h = i + 1
            
    return h # (43 ms)