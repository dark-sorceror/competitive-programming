# https://leetcode.com/problems/minimum-cost-to-convert-string-i/

def minimumCost(source: str, target: str, original: list[str], changed: list[str], cost: list[int]) -> int:
    m = [[float('inf')] * 26 for _ in range(26)]
    t = 0

    for i in range(26):
        m[i][i] = 0

    for o, c, z in zip(original, changed, cost):
        u = ord(o) - ord('a')
        v = ord(c) - ord('a')

        m[u][v] = min(m[u][v], z)
        
    # Floyd-Warshall Algorithm
    for i in range(26):
        for j in range(26):
            for k in range(26):
                if m[j][i] != float('inf') and m[i][k] != float('inf'):
                    m[j][k] = min(m[j][k], m[j][i] + m[i][k])

    for i, j in zip(source, target):
        if i == j: continue
        
        u = ord(i) - ord('a')
        v = ord(j) - ord('a')
        
        c = m[u][v]

        if c == float('inf'): return -1
        
        t += c
        
    return t # (1275 ms)