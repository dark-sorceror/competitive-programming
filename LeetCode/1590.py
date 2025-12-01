# https://leetcode.com/problems/make-sum-divisible-by-p/

def minSubarray(nums: list[int], p: int) -> int:
    t = sum(nums)
    r = t % p
    
    if r == 0: return 0

    n = len(nums)
    ml = n
    c = 0

    mi = {0: -1}

    for i in range(n):
        c = (c + nums[i]) % p
        tm = (c - r + p) % p

        if tm in mi:
            j = mi[tm]
            sl = i - j
            ml = min(ml, sl)

        mi[c] = i

    return ml if ml < n else -1 # (71 ms)