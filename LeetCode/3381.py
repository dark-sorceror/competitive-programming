# https://leetcode.com/problems/maximum-subarray-sum-with-length-divisible-by-k/

def maxSubarraySum(nums: list[int], k: int) -> int:
    n = len(nums)

    if n == 0: return 0

    ps = [0] * (n + 1)

    for i in range(n):
        ps[i + 1] = ps[i] + nums[i]

    m, h = float('-inf'), {0: 0}

    for i in range(1, n + 1):
        c, r = ps[i], i % k

        if r in h:
            sub = c - h[r]
            m = max(m, sub)

        if r not in h or c < h[r]:
            h[r] = c

    return m if m != float('-inf') else 0 # (339 ms)