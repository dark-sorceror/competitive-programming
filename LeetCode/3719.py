# https://leetcode.com/problems/longest-balanced-subarray-i/

def longestBalanced(nums: list[int]) -> int:
    n = len(nums)
    a = 0

    for i in range(n):
        c = [0, 0]
        h = set()

        for j in range(i, n):
            if nums[j] not in h:
                c[nums[j] & 1] += 1
                h.add(nums[j])

            if c[0] == c[1]:
                a = max(a, j - i + 1)
                
    return a # (1276 ms)