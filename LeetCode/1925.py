# https://leetcode.com/problems/count-square-sum-triples/

def countTriples(n: int) -> int:
    r = 0
    
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            x = a ** 2 + b ** 2
            c = int(x ** 0.5)

            if c <= n and c ** 2 == x: r += 1
                
    return r # (363 ms)