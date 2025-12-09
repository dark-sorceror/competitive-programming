# https://leetcode.com/problems/count-special-triplets/

def specialTriplets(nums: list[int]) -> int:
    n, t = len(nums), 0

    for j in range(1, n - 1):
        r, ci, ck = nums[j] * 2, 0, 0
        
        for i in range(j):
            if nums[i] == r: ci += 1

        for k in range(j + 1, n):
            if nums[k] == r: ck += 1

        t = (t + (ci * ck) % (10**9 + 7)) % (10**9 + 7)

    return t