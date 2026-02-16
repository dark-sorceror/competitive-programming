# https://leetcode.com/problems/reverse-bits/

def reverseBits(n: int) -> int:
    a = 0
    
    for i in range(32):
        a |= (n & 1) << (31 - i)
        n >>= 1

    return a # (44 ms)