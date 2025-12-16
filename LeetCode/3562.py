# https://leetcode.com/problems/maximum-profit-from-trading-stocks-with-discounts/

import math
from collections import defaultdict

def maxProfit(n: int, present: list[int], future: list[int], hierarchy: list[list[int]], budget: int) -> int:
    p = [0] + present
    f = [0] + future
    
    adj = defaultdict(list)
    
    for i, j in hierarchy:
        adj[i].append(j)
    
    # Dictionary containing both i and j trees
    m = {}

    # To calculate the maximum profit for the subtree rooted at employee x
    def dfs(x: int, is_d: bool) -> list:
        # Calculating the initial profit and cost from x's own stock purchase
        c_f = p[x]
        c_d = math.floor(p[x] / 2)
        
        # Max profit for x's subtree if they buy their stock
        mp_x_b = [-1] * (budget + 1)
        # Max profit for x's subtree if they do not buy their stock
        mp_x_nb = [0] * (budget + 1)
        
        # If x does buy:
        x_c = c_f
        x_p = f[x] - c_f
        
        if is_d and (f[x] - c_d) > x_p:
            x_c = c_d
            x_p = f[x] - c_d
            
        if x_c <= budget and x_p > 0:
            for i in range(x_c, budget + 1):
                mp_x_b[i] = x_p
        
        # If x does not buy: Loop through children of x
        for i in adj[x]:
            # Recursion to get result of a child
            mp_c_nd = dfs(i, False)
            mp_c_wd = dfs(i, True)
            
            n_mp_x_b = [-1] * (budget + 1)
            n_mp_x_nb = [-1] * (budget + 1)
            
            # If child has discount, update the segment for x's buy
            for j in range(budget + 1):
                # Knapsack loop: allocating budget k to the current child
                for k in range(budget - j + 1):
                    if mp_c_wd[k] != -1:
                        n_t = j + k
                        n_p = mp_x_b[j] + mp_c_wd[k]
                        n_mp_x_b[n_t] = max(n_mp_x_b[n_t], n_p)
            
            # Update x's buy decision list    
            mp_x_b = n_mp_x_b
            
            # If child has no discount, update the segment for x's no buy
            for j in range(budget + 1):
                c_p = mp_x_nb[j]
                
                for k in range(budget - j + 1):
                    if mp_c_nd[k] != -1:
                        n_t = j + k
                        n_p = c_p + mp_c_nd[k]
                        n_mp_x_nb[n_t] = max(n_mp_x_nb[n_t], n_p)
            
            # Update x's no buy decision list            
            mp_x_nb = n_mp_x_nb
        
        # Combine the buy and no buy profits for the final DP table    
        final = [-1] * (budget + 1)
        
        for i in range(budget + 1):
            final[i] = max(mp_x_b[i], mp_x_nb[i])
            
        m[(x, is_d)] = final
        
        return final

    r = dfs(1, False)
    
    return max(0, max(r))

n =2
present =[3,4]
future =[5,8]
hierarchy =[[1,2]]
budget =4

print(maxProfit(n, present, future, hierarchy, budget))