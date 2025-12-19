# https://leetcode.com/problems/find-all-people-with-secret/

def findAllPeople(n: int, meetings: list[list[int]], firstPerson: int) -> list[int]:
    meetings.sort(key = lambda x: x[2])
    
    k, i, nm = {0, firstPerson}, 0, len(meetings)
    
    while i < nm:
        j = i
        
        while j < nm and meetings[j][2] == meetings[i][2]:
            j += 1

        current_batch = meetings[i:j]
        
        # All meetings at a current time, anyone in a connected compoennet will konw the secret
        adj_g = {}
        inv = set()
        
        for p1, p2, t in current_batch:
            if p1 not in adj_g: adj_g[p1] = []
            if p2 not in adj_g: adj_g[p2] = []
            
            adj_g[p1].append(p2)
            adj_g[p2].append(p1)
            inv.add(p1)
            inv.add(p2)

        s = []
        
        for p in inv:
            if p in k: s.append(p)

        # dfs
        while s:
            c = s.pop()
            
            if c in adj_g:
                for n in adj_g[c]:
                    if n not in k:
                        k.add(n)
                        s.append(n)

        i = j
        
    return list(k) # (286 ms)