# https://leetcode.com/problems/greatest-sum-divisible-by-three/

def maxSumDivThree(nums: list[int]) -> int:
    t = sum(nums)

    if t % 3 == 0: return t

    r1 = sorted([i for i in nums if i % 3 == 1])
    r2 = sorted([i for i in nums if i % 3 == 2])

    if t % 3 == 1:
        o1 = r1[0] if r1 else float('inf')
        o2 = r2[0] + r2[1] if len(r2) >= 2 else float('inf')

        r = min(o1, o2)
    else:
        o1 = r2[0] if r2 else float('inf')
        o2 = r1[0] + r1[1] if len(r1) >= 2 else float('inf')

        r = min(o1, o2)

    return t - r if r != float('inf') else 0 # (15 ms)