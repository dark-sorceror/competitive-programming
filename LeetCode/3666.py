# https://leetcode.com/problems/minimum-operations-to-equalize-binary-string/

from collections import deque

class DSU:
    def __init__(self, n):
        self.parent = list(range(n + 3))
        
    def find(self, i):
        if self.parent[i] == i:
            return i

        root = i

        while self.parent[root] != root:
            root = self.parent[root]
            
        curr = i

        while curr != root:
            nxt = self.parent[curr]

            self.parent[curr] = root

            curr = nxt
            
        return root

def minOperations(s: str, k: int) -> int:
    n = len(s)
    z = s.count('0')
    
    if z == 0:
        return 0

    d = [DSU(n), DSU(n)]

    p_start = z % 2
    d[p_start].parent[z] = d[p_start].find(z + 2)
    
    q = deque([(z, 0)])
    
    while q:
        x, dist = q.popleft()
        
        y_min = max(0, x + k - n)
        y_max = min(x, k)

        z_min = x + k - 2 * y_max
        z_max = x + k - 2 * y_min
        
        p = z_min % 2
        
        c = d[p].find(z_min)

        while c <= z_max:
            if c == 0:
                return dist + 1
                
            q.append((c, dist + 1))
            
            d[p].parent[c] = d[p].find(c + 2)
            c = d[p].find(c)
            
    return -1