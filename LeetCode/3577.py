# https://leetcode.com/problems/count-the-number-of-computer-unlocking-permutations/

def countPermutations(complexity: list[int]) -> int:
    t, n = 1, len(complexity)
    
    for i in range(1, n):
        if complexity[i] <= complexity[0]: return 0
        
    for i in range(1, n):
        t = t * i % (10 ** 9 + 7)
        
    return t # (12 ms)