# https://leetcode.com/problems/number-of-ways-to-paint-n-3-grid/

def numOfWays(n: int) -> int:
    aba = 3 * 2 * 1
    abc = 3 * 2 * 1
    
    for i in range(n - 1):
        n_aba = 3 * aba + 2 * abc
        n_abc = 2 * aba + 2 * abc
        
        aba, abc = n_aba, n_abc
        
    return (aba + abc) % (10**9 + 7) # (31 ms)