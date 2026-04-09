# https://leetcode.com/problems/xor-after-range-multiplication-queries-i/

def xorAfterQueries(nums: list[int], queries: list[list[int]]) -> int:
    for l, r, k, v in queries:
        for idx in range(l, r + 1, k):
            nums[idx] = (nums[idx] * v) % (10**9 + 7)
    
    return reduce(xor, nums) # (1570 ms)