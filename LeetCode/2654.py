# https://leetcode.com/problems/minimum-number-of-operations-to-make-all-array-elements-equal-to-1/

def minOperations(nums: list[int]) -> int:
    def _gcd(a: int, b: int) -> int:
        while b:
            a, b = b, a % b

        return a

    n = len(nums)

    if n == 1: return 0 if nums[0] == 1 else -1

    gcd = nums[0]

    for i in range(1, n):
        gcd = _gcd(gcd, nums[i])
    
    c = nums.count(1)
    
    if gcd > 1: return -1
    if c >= 1: return n - c

    m = n + 1
    
    for i in range(n):
        cgcd = nums[i]
        
        for j in range(i, n):
            cgcd = _gcd(cgcd, nums[j])
            
            if cgcd == 1:
                l = j - i + 1
                m = min(m, l)

                break 

    return m + n - 2 # (0 ms)