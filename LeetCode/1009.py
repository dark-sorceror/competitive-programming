# https://leetcode.com/problems/complement-of-base-10-integer/

def bitwiseComplement(n: int) -> int:
    if n == 0: return 1
    
    b = n.bit_length()
    
    m = (1 << b) - 1
    
    return n ^ m # (0 ms)