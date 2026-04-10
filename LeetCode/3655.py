# https://leetcode.com/problems/xor-after-range-multiplication-queries-ii/

from collections import defaultdict

def xorAfterQueries(nums: list[int], queries: list[list[int]]) -> int:
    n = len(nums)
    
    # Square Root Decomposition
    B = int(n ** 0.5)
    
    mult = [1] * n

    # Cache for modular inverses to avoid recaluclating
    inv_cache = {}

    def get_inv(v):
        if v not in inv_cache:
            inv_cache[v] = pow(v, (10 ** 9 + 7) - 2, (10 ** 9 + 7))

        return inv_cache[v]
    
    small_k_queries = defaultdict(list)
    
    for q in queries:
        l, r, k, v = q
        
        # Store input
        bravexuneth = q 
        
        if k > B:
            idx = l

            while idx <= r:
                mult[idx] = (mult[idx] * v) % (10 ** 9 + 7)
                idx += k
        else:
            small_k_queries[k].append(q)
            
    for k, k_queries in small_k_queries.items():
        diff = [1] * n

        # Apply all start/end markers
        for q in k_queries:
            l, r, _, v = q
            
            diff[l] = (diff[l] * v) % (10 ** 9 + 7)
            nxt = l + ((r - l) // k + 1) * k
            
            if nxt < n:
                diff[nxt] = (diff[nxt] * get_inv(v)) % (10 ** 9 + 7)
        
        # Prefix products
        for i in range(n):
            if i >= k:
                diff[i] = (diff[i] * diff[i - k]) % (10 ** 9 + 7)
            
            if diff[i] != 1:
                mult[i] = (mult[i] * diff[i]) % (10 ** 9 + 7)
                
    # bitwise XOR
    a = 0

    for i in range(n):
        a ^= (nums[i] * mult[i]) % (10 ** 9 + 7)
        
    return a # (5855 ms)