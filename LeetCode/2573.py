# https://leetcode.com/problems/find-the-string-with-lcp/

def findTheString(lcp: list[list[int]]) -> str:
    n = len(lcp)
    s = [""] * n
    c = ord('a')
    
    for i in range(n):
        if s[i] == "":
            if c > ord('z'):
                return ""

            curr = chr(c)

            for j in range(i, n):
                if lcp[i][j] > 0:
                    s[j] = curr

            c += 1
    
    if "" in s: return ""
    a = "".join(s)
    
    for i in range(n - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            e = 0

            if a[i] == a[j]:
                e = 1 + (lcp[i + 1][j + 1] if i + 1 < n and j + 1 < n else 0)
            
            if lcp[i][j] != e:
                return ""
                
    return a # (143 ms)