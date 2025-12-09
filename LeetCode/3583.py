# https://leetcode.com/problems/count-special-triplets/

from collections import Counter

def specialTriplets(nums: list[int]) -> int:
    n, t = len(nums), 0
    rc, lc = Counter(nums[2:]), Counter([nums[0]])

    for j in range(1, n - 1):
        r = nums[j] * 2

        ci, ck = lc.get(r, 0), rc.get(r, 0)

        if ci > 0 and ck > 0:
            t = (t + (ci * ck) % (10**9 + 7)) % (10**9 + 7)
        
        lc[nums[j]] += 1

        if j + 1 < n - 1:
            nk = nums[j + 1]
            rc[nk] -= 1

            if rc[nk] == 0: del rc[nk]

    return t # (2022 ms)