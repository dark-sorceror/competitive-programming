# https://leetcode.com/problems/1-bit-and-2-bit-characters/
def isOneBitCharacter(bits: list[int]) -> bool:
    i, n = 0, len(bits)
    
    while i < n - 1:
        if bits[i] == 1: i += 2
        else: i += 1
    
    return i == n - 1 # (0 ms)