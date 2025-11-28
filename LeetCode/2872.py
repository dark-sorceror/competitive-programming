# https://leetcode.com/problems/maximum-number-of-k-divisible-components/

def maxKDivisibleComponents(n: int, edges: list[list[int]], values: list[int], k: int) -> int:
    adj = [[] for _ in range(n)]

    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    
    c = 0

    def dfs(c, cn, pn):
        cs = values[cn]

        for i in adj[cn]:
            if i != pn: cs += dfs(c, i, cn)

        if cs % k == 0: 
            c += 1
            
            return 0
        else: return cs

    dfs(c, 0, -1)
    
    return c