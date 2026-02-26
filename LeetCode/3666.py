# https://leetcode.com/problems/minimum-operations-to-equalize-binary-string/

from collections import deque

def minOperations(s: str, k: int) -> int:
    n = len(s)
    z = s.count('0')
    
    if z == 0:
        return 0

    q = deque([(z, 0)])
    v = {z}
    
    # BFS
    while q:
        curr_z, steps = q.popleft()
        
        min_j = max(0, k - (n - curr_z))
        max_j = min(curr_z, k)
        
        for j in range(min_j, max_j + 1):
            next_z = curr_z + k - 2 * j
            
            if next_z == 0:
                return steps + 1
            
            if next_z not in v:
                v.add(next_z)
                q.append((next_z, steps + 1))
                
    return -1