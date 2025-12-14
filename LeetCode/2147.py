# https://leetcode.com/problems/number-of-ways-to-divide-a-long-corridor/
    
def numberOfWays(corridor: str) -> int:
    s = [i for i, j in enumerate(corridor) if j == 'S']
    n = len(s)

    if n % 2 or n == 0: return 0

    t = 1
    
    for i in range(1, n - 1, 2):
        end, start = s[i], s[i + 1]
        g = start - end
        
        t = (t * g) % (10**9 + 7)
        
    return t # (234 ms)