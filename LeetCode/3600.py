class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.num_sets = n

    def find(self, i):
        if self.parent[i] == i:
            return i

        self.parent[i] = self.find(self.parent[i])

        return self.parent[i]

    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)

        if root_i != root_j:
            self.parent[root_i] = root_j
            self.num_sets -= 1

            return True

        return False

class Solution:
    def maxStability(self, n: int, edges: list[list[int]], k: int) -> int:
        def check(t):
            dsu = DSU(n)
            uu = 0
            ec = 0
            
            for u, v, s, m in edges:
                if m == 1:
                    if s < t: return False
                    if not dsu.union(u, v): return False

                    ec += 1
            
            for u, v, s, m in sorted(edges, key = lambda x: x[2], reverse = True):
                if m == 0:
                    if dsu.find(u) == dsu.find(v): continue
                    
                    if s >= t:
                        dsu.union(u, v)
                        ec += 1
                    elif 2 * s >= t and uu < k:
                        uu += 1
                        dsu.union(u, v)
                        ec += 1
            
            return ec == n - 1

        l, r = 1, 2 * 10 ** 9
        a = -1
        
        while l <= r:
            m = (l + r) // 2

            if check(m):
                a = m
                l = m + 1
            else:
                r = m - 1
                
        return a # (2756 ms)