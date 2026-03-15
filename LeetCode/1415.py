# https://leetcode.com/problems/the-k-th-lexicographical-string-of-all-happy-strings-of-length-n/

def getHappyString(n: int, k: int) -> str:
    r = []
    
    def backtrack(c):
        if len(c) == n:
            r.append(c)
            
            return
        
        for i in ['a', 'b', 'c']:
            if not c or c[-1] != i:
                backtrack(c + i)
    
    backtrack("")
    
    r.sort()
    
    return r[k-1] if k <= len(r) else "" # (47 ms)