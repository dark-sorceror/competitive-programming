import collections

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, i):
        if self.parent[i] == i: return i

        self.parent[i] = self.find(self.parent[i])

        return self.parent[i]

    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)

        if root_i != root_j:
            self.parent[root_i] = root_j

class Solution:
    def minimumHammingDistance(self, source: list[int], target: list[int], allowedSwaps: list[list[int]]) -> int:
        n = len(source)
        uf = UnionFind(n)
        a = 0
        c = collections.defaultdict(list)

        for i, j in allowedSwaps:
            uf.union(i, j)

        for i in range(n):
            c[uf.find(i)].append(i)
        
        for i in c:
            ci = c[i]
            s = collections.Counter(source[j] for j in ci)
            
            for j in ci:
                if s[target[j]] > 0:
                    s[target[j]] -= 1
                else:
                    a += 1

        return a # (249 ms)