# https://leetcode.com/problems/count-partitions-with-max-min-difference-at-most-k/

def countPartitions(nums: list[int], k: int) -> int: 
    n = len(nums)

    vp = [0] * (n + 1)
    vp[0] = 1

    for i in range(1, n + 1):
        c_max, c_min = nums[i - 1], nums[i - 1]

        for j in range(i):
            c_max = max(c_max, nums[j])
            c_min = min(c_min, nums[j])

            if (c_max - c_min) <= k:
                vp[i] = (vp[i] + vp[j]) % (10**9 + 7)
                
    return vp[n]