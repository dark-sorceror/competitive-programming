# https://leetcode.com/problems/k-th-smallest-in-lexicographical-order/

def findKthNumber(n: int, k: int) -> int:
    c, q = 1, []

    for i in range(n):
        q.append(c)
        
        if c * 10 <= n:
            c *= 10
        
        elif c % 10 != 9 and c + 1 <= n:
            c += 1
        
        else:
            while c // 10 > 0 and (c % 10 == 9 or c + 1 > n):
                c //= 10
                
            c += 1

    return q[k - 1]