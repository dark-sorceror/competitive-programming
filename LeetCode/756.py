# https://leetcode.com/problems/pyramid-transition-matrix/

from collections import defaultdict

def pyramidTransition(bottom: str, allowed: list[str]) -> bool:
    t = defaultdict(list) # (l, r) -> list of allowed
    
    for i in allowed:
        t[(i[0], i[1])].append(i[2])

    m = {}

    def solve(row: str):
        if len(row) == 1: return True
        if row in m: return m[row]
        
        def next_row(i, n_row):
            if i == len(row) - 1: return solve("".join(n_row))
            
            l, r = row[i], row[i + 1]

            for j in t[(l, r)]:
                n_row.append(j)
                
                if next_row(i + 1, n_row): return True
                n_row.pop()
            
            return False

        o = next_row(0, [])
        m[row] = o
        
        return o

    return solve(bottom) # (270 ms)