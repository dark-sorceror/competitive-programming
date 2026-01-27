# https://leetcode.com/problems/minimum-cost-path-with-edge-reversals/

import heapq
from collections import defaultdict

def minCost(n: int, edges: list[list[int]]) -> int:
    g = defaultdict(list)

    for u, v, w in edges:
        g[u].append((v, w))
        g[v].append((u, 2 * w))

    pq = [(0, 0)]

    m = [float('inf')] * n
    m[0] = 0
    
    # Dijkstra's Algorithm
    while pq:
        c, u = heapq.heappop(pq)

        if u == n - 1:
            return c

        if c > m[u]:
            continue
        
        for i, j in g[u]:
            if (c + j) < m[i]:
                m[i] = c + j
                heapq.heappush(pq, (m[i], i))
                
        return -1