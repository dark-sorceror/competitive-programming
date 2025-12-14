# https://leetcode.com/problems/number-of-ways-to-divide-a-long-corridor/
    
def numberOfWays(corridor: str) -> int:
    s = [i for i, j in enumerate(corridor) if j == 'S']
    n = len(s)

    t = 0
    
    for i in range(1, n - 1, 2):
        end = s[i]
        start = s[i + 1]

        g = start - end
        
        t = (t * g) % (10**9 + 7)
        
    return t