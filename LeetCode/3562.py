# https://leetcode.com/problems/maximum-profit-from-trading-stocks-with-discounts/

from collections import defaultdict

def maxProfit(n: int, present: list[int], future: list[int], hierarchy: list[list[int]], budget: int) -> int:
    P = [0] + present
    F = [0] + future
    
    adj_g = defaultdict(list)
    
    for i, j in hierarchy:
        adj_g[i].append(j)
    
    # Dictionary containing both i and j trees
    m = {}
    
    def merge(a: dict, b: dict) -> dict:
        r = {}
        
        # budget, profit
        for b_a, p_a in a.items():
            for b_b, p_b in b.items():
                tb = b_a + b_b
                
                if tb <= budget:
                    r[tb] = max(
                        r.get(tb, float('-inf')), p_a + p_b
                    )
                    
        return r

    # To calculate the maximum profit for the subtree rooted at employee i using dfs
    def dfs(i: int, is_d: bool) -> list:
        # Check memoization for optimization
        if (i, is_d) in m: return m[(i, is_d)]

        nb = {0: 0}
        bf = {}
        bd = {}
        f = {}
        
        c = P[i]
        p = F[i] - c
        
        if c <= budget: bf[c] = p
            
        if is_d:
            c = P[i] // 2
            p = F[i] - c
            
            if c <= budget: bd[c] = p

        # Merge children
        for c in adj_g[i]:
            c_nd = dfs(c, False)
            c_wd = dfs(c, True)

            nb = merge(nb, c_nd)

            cc = {}
            
            for i in set(c_nd.keys()).union(c_wd.keys()):
                # Get the best result from the child choosing to use discount or not buying at all
                cc[i] = max(
                    c_nd.get(i, float('-inf')), 
                    c_wd.get(i, float('-inf'))
                )
                
            bf = merge(bf, cc)
            bd = merge(bd, cc)
        
        # Combine results from each segment
        for d in [nb, bf, bd]:
            for k, v in d.items():
                f[k] = max(f.get(k, float('-inf')), v)

        m[(i, is_d)] = f
        
        return f

    r = dfs(1, False)
    
    return max(r.values()) # (2232 ms)