# https://leetcode.com/problems/power-grid-maintenance/

from collections import defaultdict
import heapq

def processQueries(c: int, connections: list[list[int]], queries: list[list[int]]) -> list[int]:
    p, ct, co, o, r = list(range(c + 1)), defaultdict(list), {}, [True] * (c + 1), []
    
    def find(i):
        if i == p[i]: return i
        return find(p[i])
    
    def union(i, j):
        i = find(i)
        j = find(j)
        
        if i != j:
            p[j] = i
            
            return True
        
        return False
    
    for u, v in connections:
        union(u, v)
    
    for i in range(1, c + 1):
        ct[find(i)].append(i)
        
    co = {}
    
    for i, j in ct.items():
        heap = j[:]
        heapq.heapify(heap)
        co[i] = heap
    
    for i, j in queries:
        root = find(j)

        if i == 1:
            if o[j]:
                r.append(j)
                
                continue
            
            heap = co[root]
            
            while heap and not o[heap[0]]:
                heapq.heappop(heap)
            if heap:
                r.append(heap[0])
            else:
                r.append(-1)

        else:
            if o[j]:
                o[j] = False
            
    return r

c =2
connections =[[2,1]]
queries =[[1,1],[1,2],[1,2],[2,2],[1,2],[2,1],[1,2],[2,1],[2,1],[1,1]]

print(processQueries(c, connections, queries))