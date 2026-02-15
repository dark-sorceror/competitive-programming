# https://leetcode.com/problems/add-binary/

def addBinary(a: str, b: str) -> str:
    r = []
    c = 0

    i, j = len(a) - 1, len(b) - 1
    
    while i >= 0 or j >= 0 or c:
        d_a = int(a[i]) if i >= 0 else 0
        d_b = int(b[j]) if j >= 0 else 0
        
        t = d_a + d_b + c
        c = t // 2
        r.append(str(t % 2))
        
        i -= 1
        j -= 1

    return "".join(r[::-1]) # (0 ms)