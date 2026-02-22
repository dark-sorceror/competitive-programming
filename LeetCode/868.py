# https://leetcode.com/problems/binary-gap/

def binaryGap(n: int) -> int:
    b = bin(n)[2:]

    m = 0
    p = None
    
    for i, j in enumerate(b):
        if j == '1':
            if p is not None:
                m = max(m, i - p)

            p = i
            
    return m # (0 ms)