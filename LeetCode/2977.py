# https://leetcode.com/problems/minimum-cost-to-convert-string-ii/

def minimumCost(source: str, target: str, original: list[str], changed: list[str], cost: list[int]) -> int:
    s = {}
    u = set(original) | set(changed)

    for i in u:
        s[i] = len(s)
    
    n = len(s)
    
    d = [[float('inf')] * n for i in range(n)]
    
    for i in range(n):
        d[i][i] = 0
        
    for i, j, k in zip(original, changed, cost):
        u, v = s[i], s[j]
        d[u][v] = min(d[u][v], k)
        
    # Floyd-Warshall Algorithm
    for i in range(n):
        for j in range(n):
            if d[j][i] == float('inf'): continue
            for k in range(n):
                if d[i][k] == float('inf'): continue
                d[j][k] = min(d[j][k], d[j][i] + d[i][k])
        
    p = set(len(i) for i in original)

    dp = [float('inf')] * (len(source) + 1)
    dp[0] = 0
    
    # Dynamic Programming
    for i in range(len(source)):
        if dp[i] == float('inf'): continue
        
        if source[i] == target[i]:
            dp[i + 1] = min(dp[i + 1], dp[i])
        
        for j in p:
            k = i + j

            if k > len(source): continue
            
            s_s = source[i:k]
            s_t = target[i:k]
            
            if s_s in s and s_t in s:
                u = s[s_s]
                v = s[s_t]

                if d[u][v] != float('inf'):
                    dp[k] = min(dp[k], dp[i] + d[u][v])
        
    return dp[len(source)] if dp[len(source)] != float('inf') else -1 # (938 ms)