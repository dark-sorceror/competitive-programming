# https://leetcode.com/problems/power-grid-maintenance/

def processQueries(c: int, connections: list[list[int]], queries: list[list[int]]) -> list[int]:
    p, g, o, r = list(range(c + 1)), [1] * (c + 1), [True] * (c + 1), []
    
    def find(i):
        if i == p[i]: return i
        return find(p[i])
    
    def union(i, j):
        i = find(i)
        j = find(j)
        
        if i != j:
            p[j] = i
            g[i] += 1
            
            return True
        
        return False
    
    for u, v in connections:
        union(u, v)
    
    for i, j in queries:
        root = find(j)

        if i == 1:
            if o[j]:
                r.append(j)
                
                continue
            
            if g[root] >= 1:
                r.append(o[root:].index(max(o[root:])) + root)
            
            if g[root] <= 0: r.append(-1)
        else:
            g[root] -= 1
            o[j] = False
            
    return r