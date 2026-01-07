# https://leetcode.com/problems/product-of-array-except-self/

def productExceptSelf(nums: list[int]) -> list[int]:
    n = len(nums)
    a = [0] * n
    l = r = 1

    for i, j in enumerate(nums):
        a[i] = l
        l *= j
    
    for i in range(n - 1, -1, -1):
        a[i] *= r
        r *= nums[i]

    return a # (15 ms)