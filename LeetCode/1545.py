# https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/

def findKthBit(self, n: int, k: int) -> str:
    if n == 1:
        return "0"
    
    l = (1 << n) - 1
    m = (l // 2) + 1
    
    if k == m:
        return "1"
    elif k < m:
        return self.findKthBit(n - 1, k)
    else:
        new_k = l - k + 1
        
        return '1' if self.findKthBit(n - 1, new_k) == '0' else '0' # (0 ms)