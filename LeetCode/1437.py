# https://leetcode.com/problems/check-if-all-1s-are-at-least-length-k-places-away/

def kLengthApart(nums: list[int], k: int) -> bool:
    p = None
    
    for i, j in enumerate(nums):
        if j == 1:
            if p is not None and i - p - 1 < k: return False

            p = i
    
    return True # (3 ms)