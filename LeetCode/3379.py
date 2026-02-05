# https://leetcode.com/problems/transformed-array/

def constructTransformedArray(nums: list[int]) -> list[int]:
    n = len(nums)
    r = [0] * n

    for i in range(n):
        r[i] = nums[(i + nums[i]) % n]

    return r # (56 ms)