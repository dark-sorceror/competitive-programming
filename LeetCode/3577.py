# https://leetcode.com/problems/count-the-number-of-computer-unlocking-permutations/

def countPermutations(complexity: list[int]) -> int:
    t = 1
    n = len(complexity)
    p = [set() for i in complexity]
    
    for i in range(1, n):
        for j in range(i):
            if complexity[j] < complexity[i]:
                p[i].add(j)
        
    u = {0}
    r = set()
    
    for i in range(1, n):
        if 0 in p[i]:
            r.add(i)
            
    for i in range(1, n):
        c = 1
        
        t = (t * c) % (10 ** 9 + 7)
        
        k = next(iter(r))
        r.remove(k)
        u.add(k)
        
    return t